import vanilla
import os
from AppKit import *
from mojo.events import addObserver, removeObserver
from mojo.UI import GetFile


"""
Scale and Adjust glyphs
2019_09_24 Andy Clymer

"""



LIBKEY = "com.andyclymer.ScaleAndAdjustSettings"


""" Helpers """


def measureStems(f):
    # Get a rough measurement of H and V stems, using the UC and LC "O"
    # Return None if it's unable to measure the stems (the glyphs don't exist or aren't made up of 2 contours)
    stems = dict(lc=None, uc=None)
    for gn in ["O", "o"]:
        g = None
        if gn in f.keys():
            g = f[gn].copy()
            if len(g.contours) == 2:
                g.extremePoints()
                vertBounds = [g.contours[0].bounds[0], g.contours[1].bounds[0]]
                vertBounds.sort()
                vert = vertBounds[1] - vertBounds[0]
                horizBounds = [g.contours[0].bounds[1], g.contours[1].bounds[1]]
                horizBounds.sort()
                horiz = horizBounds[1] - horizBounds[0]
                if gn == "o":
                    key = "lc"
                else: key = "uc"
                stems[key] = dict(horiz=horiz, vert=vert)
    return stems


def interpolate(f, a, b):
    return a + (b - a) * f
    

def colorText(text, color="black", sizeStyle="regular", style=None):
    """
    colorText(text, color="black", size="regular", style=None)
    
        color = red, green, blue, cyan, magenta, yellow, gray, lightGray
        sizeStyle = regular, small, mini
        style = regular, bold
    
    Returns a NSAttributedString with color and style for use in an interface
    
    Note: Concotanate two NSMUtableAttributedStrings like so:
        text = ColorText("testing", color="red")
        text2 = ColorText("more testing", color="green")
        text.appendAttributedString_(text2)
    """
    
    sizeStyleMap = {
        "regular":  NSRegularControlSize,
        "small":    NSSmallControlSize,
        "mini":     NSMiniControlSize}
    colors = {
        "red":      NSColor.redColor(),
        "green":    NSColor.greenColor(),
        "blue":     NSColor.blueColor(),
        "cyan":     NSColor.cyanColor(),
        "magenta":  NSColor.magentaColor(),
        "yellow":   NSColor.yellowColor(),
        "gray":     NSColor.grayColor(),
        "lightGray":NSColor.lightGrayColor()}
    attrs = {}
    
    if sizeStyle in sizeStyleMap:
        nsSizeConstant = sizeStyleMap[sizeStyle]
    else: nsSizeConstant = sizeStyleMap["regular"]
    
    # Color attribute
    if color in colors:
        attrs[NSForegroundColorAttributeName] = colors[color]
    # Font style attribute   
    if style == "bold":
        attrs[NSFontAttributeName] = NSFont.boldSystemFontOfSize_(NSFont.systemFontSizeForControlSize_(nsSizeConstant))
    else:
        attrs[NSFontAttributeName] = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(nsSizeConstant))
    # Build the string with these attributes:
    string = NSMutableAttributedString.alloc().initWithString_attributes_(text, attrs)

    return string


def collectGroups(f):
    fontName = f.info.postscriptFontName
    groups = []
    groupNames = f.groups.keys()
    groupNames.sort()
    for groupName in groupNames:
        if not groupName.startswith("public.kern"):
            glyphNames = f.groups[groupName]
            #fullGroupName = "%s: %s (%s glyphs)" % (fontName, groupName, glyphCount)
            fullGroupName = "%s: %s" % (fontName, groupName)
            groups.append(dict(name=fullGroupName, glyphNames=glyphNames))
    return groups
    
    

""" Window """    

class ScaleAndAdjust:
    
    def __init__(self):
        
        self.fontList = []
        self.fontNames = []
        self.fontStems = []
        self.estimatedStems = None # Estimated stem measurements for the resulting font
        
        # Glyph groups
        self.groups = []
        
        # Case info, normalized after editing
        self.normalizedInfo = {}
        self.dataNorms = {
            "scaleH": dict(default=100, dataType=float, scale=0.01),
            "scaleV": dict(default=100, dataType=float, scale=0.01),
            "interpH": dict(default=100, dataType=float, scale=0.01),
            "interpV": dict(default=100, dataType=float, scale=0.01),
            "tracking": dict(default=0, dataType=float, scale=1)}
        
        self.w = vanilla.Window((300, 880), "Scale And Interpolate")
        step = 10
        self.w.font0title = vanilla.TextBox((10, step, -10, 25), colorText("Lightest Master (0%)", style="bold"))
        self.w.font0choice = vanilla.PopUpButton((10, step+20, -10, 25), self.fontNames, callback=self.fontChoiceChanged)
        step += 50
        self.w.font0stemTextUC = vanilla.TextBox((20, step, -10, 20), "")
        self.w.font0stemTextLC = vanilla.TextBox((20, step+20, -10, 20), "")
        step += 50
        self.w.font1title = vanilla.TextBox((10, step, -10, 25), colorText("Heaviest Master (100%)", style="bold"))
        self.w.font1choice = vanilla.PopUpButton((10, step+20, -10, 25), self.fontNames, callback=self.fontChoiceChanged)
        step += 50
        self.w.font1stemTextUC = vanilla.TextBox((20, step, -10, 20), "")
        self.w.font1stemTextLC = vanilla.TextBox((20, step+20, -10, 20), "")
        step += 50
        
        self.w.hr1 = vanilla.HorizontalLine((10, step, -10, 1))
        
        step += 15
        self.w.capsTitle = vanilla.TextBox((10, step, -10, 25), colorText("Caps", style="bold"))
        step += 25
        self.w.ucGroups = vanilla.PopUpButton((10, step, -10, 25), [])
        step += 35
        columnDescriptions = [dict(title="Name"), dict(title="Value", editable=True, width=50)]
        capInfo = [
            dict(Name="Scale Horizontal %", attr="scaleH", Value=100),
            dict(Name="Scale Vertical %", attr="scaleV", Value=100),
            dict(Name="Interpolate Horizontal %", attr="interpH", Value=100),
            dict(Name="Interpolate Vertical %", attr="interpV", Value=100),
            dict(Name="Units of tracking", attr="tracking", Value=0)]
        self.w.ucInfo = vanilla.List((10, step, -10, 100), capInfo, columnDescriptions=columnDescriptions, showColumnTitles=False, editCallback=self.dataChanged)
        step += 110
        self.w.resultStemTextUC = vanilla.TextBox((20, step, -10, 20), "")
        step += 30
        
        self.w.lcTitle = vanilla.TextBox((10, step, -10, 25), colorText("Lowercase", style="bold"))
        step += 25
        self.w.lcGroups = vanilla.PopUpButton((10, step, -10, 25), [])
        step += 35
        lcInfo = [
            dict(Name="Scale Horizontal %", attr="scaleH", Value=100),
            dict(Name="Scale Vertical %", attr="scaleV", Value=100),
            dict(Name="Interpolate Horizontal %", attr="interpH", Value=100),
            dict(Name="Interpolate Vertical %", attr="interpV", Value=100),
            dict(Name="Units of tracking", attr="tracking", Value=0)]
        self.w.lcInfo = vanilla.List((10, step, -10, 100), lcInfo, columnDescriptions=columnDescriptions, showColumnTitles=False, editCallback=self.dataChanged)
        step += 110
        self.w.resultStemTextLC = vanilla.TextBox((20, step, -10, 20), "")
        step += 30
        
        self.w.otherTitle = vanilla.TextBox((10, step, -10, 25), colorText("Other glyphs", style="bold"))
        step += 25
        self.w.otherRadio = vanilla.RadioGroup((10, step, -10, 70), 
            ["Copy from the lightest master", 
            "Process at 50% of UC and LC settings", 
            "Skip any other glyphs"], callback=self.dataChanged)
        self.w.otherRadio.set(2)
        
        step += 80
        
        self.w.loadButton = vanilla.SquareButton((100, step, -10, 25), "Load settings from UFO", callback=self.loadSettings)
        step += 35
        
        self.w.hr2 = vanilla.HorizontalLine((10, step, -10, 1))
        step += 15
        self.w.skewBox = vanilla.CheckBox((10, step, -10, 25), "Skew Italic glyphs upright before scaling")
        self.w.skewBox.set(True)
        step += 25
        self.w.infoBox = vanilla.CheckBox((10, step, -10, 25), "Interpolate Font Info whenever possible")
        self.w.infoBox.set(True)
    
        step += 40
        self.w.buildButton = vanilla.SquareButton((10, step, -10, 25), "Make Font", callback=self.makeFontCallback)
        
        # Update the font info before opening
        self.fontsChanged()
        self.dataChanged()
        
        addObserver(self, "fontsChanged", "fontDidOpen")
        addObserver(self, "fontsChanged", "newFontDidOpen")
        addObserver(self, "fontsChanged", "fontDidClose")
        self.w.bind("close", self.windowClosed)
        self.w.open()
    
    
    def windowClosed(self, sender=None):
        # Remove observers
        removeObserver(self, "fontDidOpen")
        removeObserver(self, "newFontDidOpen")
        removeObserver(self, "fontDidClose")
    
    
    def fontsChanged(self, sender=None):
        # Hold aside all dropdown choices by name
        # Get the choice indices and then turn them into strings
        font0choice = self.w.font0choice.get()
        if font0choice >= 0: font0choice = self.fontNames[font0choice]
        font1choice = self.w.font1choice.get()
        if font1choice >= 0: font1choice = self.fontNames[font1choice]
        ucGroupsChoice = self.w.ucGroups.get()
        if ucGroupsChoice >= 0: ucGroupsChoice = self.w.ucGroups.getItems()[ucGroupsChoice]
        lcGroupsChoice = self.w.lcGroups.get()
        if lcGroupsChoice >= 0: lcGroupsChoice = self.w.lcGroups.getItems()[lcGroupsChoice]
                
        # Collect font info
        self.fontNames = []
        self.fontList = []
        self.fontStems = []
        for f in AllFonts():
            name = f.info.postscriptFontName
            if name == None:
                name = f.info.fullName
                if name == None:
                    name = "(Untitled Font)"
            name = str(name)
            if not name in self.fontNames:
                self.fontNames.append(name)
                self.fontList.append(f)
                self.fontStems.append(measureStems(f))
                
        # Collect group names
        self.groups = [dict(name="(No group)", glyphNames=[])]
        for font in self.fontList:
            self.groups += collectGroups(font)
        groupNames = [item["name"] for item in self.groups]
        
        # Update the group dropdowns and try to select the previous choice
        
        # Font0
        self.w.font0choice.setItems(self.fontNames)
        if font0choice in self.fontNames:
            idx = self.fontNames.index(font0choice)
        else: idx = 0
        self.w.font0choice.set(idx)
        # Font1
        self.w.font1choice.setItems(self.fontNames)
        if font1choice in self.fontNames:
            idx = self.fontNames.index(font1choice)
        else: idx = 0
        self.w.font1choice.set(idx)
        # ucGroups
        self.w.ucGroups.setItems(groupNames)
        if ucGroupsChoice in groupNames:
            idx = groupNames.index(ucGroupsChoice)
        else: idx = 0
        self.w.ucGroups.set(idx)
        # lcGroups
        self.w.lcGroups.setItems(groupNames)
        if lcGroupsChoice in groupNames:
            idx = groupNames.index(lcGroupsChoice)
        else: idx = 0
        self.w.lcGroups.set(idx)
                
        # And update other font settings
        self.dataChanged()
    

    def fontChoiceChanged(self, sender=None):
        # Font choice changed
        font0Idx = self.w.font0choice.get()
        font1Idx = self.w.font1choice.get()
        
        # Update the stem measurement
        self.estimateStems()
        
        # Reset the stem descriptions
        self.w.font0stemTextUC.set(colorText("UC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.w.font0stemTextLC.set(colorText("LC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.w.font1stemTextUC.set(colorText("UC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.w.font1stemTextLC.set(colorText("LC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.w.resultStemTextUC.set(colorText("UC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.w.resultStemTextLC.set(colorText("LC stems: (Uncertain)", color="gray", sizeStyle="small"))
        
        if font0Idx > -1 and font1Idx > -1:
            font0 = self.fontList[font0Idx]
            font1 = self.fontList[font1Idx]
            
            # Update stem descriptions for the selected fonts
            for fontIdx in range(2):
                if fontIdx == 0:
                    stems = self.fontStems[font0Idx]
                else: stems = self.fontStems[font1Idx]
                if stems:
                    stemsText = []
                    for case in ["uc", "lc"]:
                        stemText = "%s stems: " % case.upper()
                        if case in stems:
                            if not stems[case] == None:
                                stemText += "%s horizontal, %s vertical" % (stems[case]["horiz"], stems[case]["vert"])
                            else: stemText += "(Uncertain)"
                        stemsText.append(colorText(stemText, color="gray", sizeStyle="small"))
                    if fontIdx == 0:
                        self.w.font0stemTextUC.set(stemsText[0])
                        self.w.font0stemTextLC.set(stemsText[1])
                    else:
                        self.w.font1stemTextUC.set(stemsText[0])
                        self.w.font1stemTextLC.set(stemsText[1])
                    
            # Updated estimated stem descriptions
            if not self.estimatedStems == None:
                for case in ["uc", "lc"]:
                    stems = self.estimatedStems[case]
                    if stems:
                        stemText = "%s stems: " % case.upper()
                        stemText += "%s horizontal, %s vertical" % (stems["horiz"], stems["vert"])
                        if case == "uc":
                            self.w.resultStemTextUC.set(colorText(stemText, color="gray", sizeStyle="small"))
                        else: self.w.resultStemTextLC.set(colorText(stemText, color="gray", sizeStyle="small"))


    
    def dataChanged(self, sender=None):
        # Data settings changed, normalize it all and hold it aside
        
        self.normalizedInfo = dict(uc=dict(problem=False), lc=dict(problem=False), other=dict(problem=False))
        
        # Run through the cases
        for case in ["uc", "lc"]:
            # Collect data
            if case == "uc":
                INFOLIST = self.w.ucInfo
            else: INFOLIST = self.w.lcInfo
            # Normalize the data
            for item in INFOLIST.get():
                default = self.dataNorms[item["attr"]]["default"]
                dataType = self.dataNorms[item["attr"]]["dataType"]
                dataScale = self.dataNorms[item["attr"]]["scale"]
                try:
                    self.normalizedInfo[case][item["attr"]] = dataType(item["Value"]) * dataScale
                except:
                    self.normalizedInfo[case][item["attr"]] = default
                    self.normalizedInfo[case]["problem"] = True
        # Build the "other" case
        otherChoice = self.w.otherRadio.get()
        if otherChoice == 1:
            otherInterp = 0.5
        else: otherInterp = 0
        for key in self.dataNorms.keys():
            if key in self.normalizedInfo["uc"] and key in self.normalizedInfo["lc"]:
                self.normalizedInfo["other"][key] = interpolate(otherInterp, self.normalizedInfo["uc"][key], self.normalizedInfo["lc"][key])
            else: self.normalizedInfo["other"][key] = self.dataNorms[key]["default"] * self.dataNorms[key]["scale"]
        # Update the test font stems
        self.estimateStems()
        # and update the UI
        self.fontChoiceChanged()
    
    
    def estimateStems(self):
        # Make a test font for the purpose of measuring stems
        if not len(self.fontList):
            self.estimatedStems = None
        else:
            font0Idx = self.w.font0choice.get()
            font1Idx = self.w.font1choice.get()
            font0 = self.fontList[font0Idx]
            font1 = self.fontList[font1Idx]
            destFont = NewFont(showInterface=False)
        
            for case in ["uc", "lc"]:
                if case == "uc":
                    gName = "O"
                else: gName = "o"
            
                CASEINFO = self.normalizedInfo[case]

                if gName in font0 and gName in font1:
                    # Copy each glyph
                    g0 = font0[gName].copy()
                    g1 = font1[gName].copy()
                    # Interpolate
                    destGlyph = destFont.newGlyph(gName)
                    destGlyph = destFont[gName]
                    destGlyph.interpolate((CASEINFO["interpH"], CASEINFO["interpV"]), g0, g1)
                    # Scale
                    destGlyph.scaleBy((CASEINFO["scaleH"], CASEINFO["scaleV"]))
                
            stems = measureStems(destFont)
            destFont.close()
            self.estimatedStems = stems


                
    def loadSettings(self, sender):
        filePath = GetFile(message="Choose a previously processed UFO to load the settings back out of", fileTypes=["ufo"])
        if not filePath == None:
            prevFont = OpenFont(filePath, showInterface=False)
            if LIBKEY in prevFont.lib.keys():
                libData = prevFont.lib[LIBKEY]
                self.w.otherRadio.set(libData["otherOption"])
                self.w.skewBox.set(libData["skewOption"])
                self.w.infoBox.set(libData["infoOption"])
                # Apply the normalized info
                for case in ["uc", "lc"]:
                    scaleH = libData["normalizedInfo"][case]["scaleH"] / self.dataNorms["scaleH"]["scale"]
                    scaleV = libData["normalizedInfo"][case]["scaleV"] / self.dataNorms["scaleV"]["scale"]
                    interpH = libData["normalizedInfo"][case]["interpH"] / self.dataNorms["interpH"]["scale"]
                    interpV = libData["normalizedInfo"][case]["interpV"] / self.dataNorms["interpV"]["scale"]
                    tracking = libData["normalizedInfo"][case]["tracking"] / self.dataNorms["tracking"]["scale"]
                    info = [
                        dict(Name="Scale Horizontal %", attr="scaleH", Value=scaleH),
                        dict(Name="Scale Vertical %", attr="scaleV", Value=scaleV),
                        dict(Name="Interpolate Horizontal %", attr="interpH", Value=interpH),
                        dict(Name="Interpolate Vertical %", attr="interpV", Value=interpV),
                        dict(Name="Units of tracking", attr="tracking", Value=tracking)]
                    if case == "uc":
                        self.w.ucInfo.set(info)
                    else: self.w.lcInfo.set(info)
                # Reset the dropdown choices
                self.w.font0choice.set(-1)
                self.w.font1choice.set(-1)
                self.w.ucGroups.set(0)
                self.w.lcGroups.set(0)
        
            prevFont.close()
        
        
        
    def makeFontCallback(self, sender):
        # Validate data
        ready = True
        font0Idx = self.w.font0choice.get()
        font1Idx = self.w.font1choice.get()
        if not -1 in [font0Idx, font1Idx]:
            if font0Idx == font1Idx:
                ready = False
                print("Choose two different fonts")
        else:
            ready = False
            print("Choose two fonts")
        # Groups
        group0Idx = self.w.ucGroups.get()
        group1Idx = self.w.lcGroups.get()
        if not -1 in [group0Idx, group1Idx]:
            if group0Idx == group1Idx:
                ready = False
                print("Choose two different groups")
        else:
            ready = False
            print("Choose two groups")
        # Ready?
        if ready:
            self.doMakeFont()
        
    
    def doMakeFont(self):
        # Make a new font
        font0Idx = self.w.font0choice.get()
        font1Idx = self.w.font1choice.get()
        font0 = self.fontList[font0Idx]
        font1 = self.fontList[font1Idx]
        destFont = NewFont(showInterface=False)
        
        # Fetch the charsets
        groupChoiceIdxUC = self.w.ucGroups.get()
        groupChoiceIdxLC = self.w.lcGroups.get()
        charsetUC = self.groups[groupChoiceIdxUC]["glyphNames"]
        charsetLC = self.groups[groupChoiceIdxLC]["glyphNames"]
        # Collect an "other" charset
        charsetOther = []
        if not self.w.otherRadio.get() == 2: # 2 = Skip
            for gn in font0.keys():
                if gn in font1.keys():
                    if not True in [gn in charsetUC, gn in charsetLC]:
                        charsetOther.append(gn)
                    
        # Font info
        destFont.info.unitsPerEm = font0.info.unitsPerEm
        
        charMap = font0.getCharacterMapping()
        
        for case in ["uc", "lc", "other"]:
            
            CASEINFO = self.normalizedInfo[case]
            if case == "uc":
                CHARSET = charsetUC
            elif case == "lc":
                CHARSET = charsetLC
            else: CHARSET = charsetOther
                    
            # Process the glyphs
            for gName in CHARSET:
                if gName in font0 and gName in font1:
                    
                    # Copy each glyph
                    g0 = font0[gName].copy()
                    g1 = font1[gName].copy()
                    
                    # Skew the glyph if the font has an Italic angle
                    if self.w.skewBox.get():
                        angle0 = font0.info.italicAngle
                        if not angle0: angle0 = 0
                        g0.skewBy(angle0)
                        angle1 = font1.info.italicAngle
                        if not angle1: angle1 = 0
                        g1.skewBy(angle1)
                    
                    # Interpolate
                    destGlyph = destFont.newGlyph(gName)
                    destGlyph = destFont[gName]
                    destGlyph.interpolate((CASEINFO["interpH"], CASEINFO["interpV"]), g0, g1)
                    
                    # Scale
                    destGlyph.scaleBy((CASEINFO["scaleH"], CASEINFO["scaleV"]))
                    destGlyph.width = int(round(destGlyph.width * CASEINFO["scaleH"]))
                    
                    # Interpolate the Italic Angle and skew back
                    if self.w.skewBox.get():
                        if not (angle0, angle1) == (0, 0):
                            f = (CASEINFO["interpH"] + CASEINFO["interpV"]) * 0.5
                            interpAngle = interpolate(f, angle0, angle1)
                            destGlyph.skewBy(-interpAngle)
                    
                    # Track
                    if destGlyph.leftMargin:
                        destGlyph.leftMargin += int(round(CASEINFO["tracking"]*0.5))
                        destGlyph.rightMargin += int(round(CASEINFO["tracking"]*0.5))
                    else: destGlyph.width += CASEINFO["tracking"]
                    
                    # Done
                    destGlyph.markColor = None
                    destGlyph.changed()
        
        # Start the Font Info
        # ...and interpolate/scale a few values
        copyAttrs = ["familyName"]
        if self.w.infoBox.get():
            # Copy some attributes
            for attr in copyAttrs:
                setattr(destFont.info, attr, getattr(font0.info, attr))
            # Interpolate and scale other attributes
            capHeight = interpolate(self.normalizedInfo["uc"]["interpV"], font0.info.capHeight, font1.info.capHeight)
            capHeight *= self.normalizedInfo["uc"]["scaleV"]
            destFont.info.capHeight = capHeight
            xHeight = interpolate(self.normalizedInfo["lc"]["interpV"], font0.info.xHeight, font1.info.xHeight)
            xHeight *= self.normalizedInfo["lc"]["scaleV"]
            destFont.info.xHeight = xHeight
            ascender = interpolate(self.normalizedInfo["lc"]["interpV"], font0.info.ascender, font1.info.ascender)
            ascender *= self.normalizedInfo["lc"]["scaleV"]
            destFont.info.ascender = ascender
            descender = interpolate(self.normalizedInfo["lc"]["interpV"], font0.info.descender, font1.info.descender)
            descender *= self.normalizedInfo["lc"]["scaleV"]
            destFont.info.ascender = descender
            
        
        # Save the settings to the font.lib
        libData = dict(
            normalizedInfo=self.normalizedInfo,
            otherOption=self.w.otherRadio.get(),
            skewOption=self.w.skewBox.get(),
            infoOption=self.w.infoBox.get())
        destFont.lib[LIBKEY] = libData

        # Finish and open the font
        destFont.glyphOrder = font0.glyphOrder
        destFont.openInterface()


ScaleAndAdjust()