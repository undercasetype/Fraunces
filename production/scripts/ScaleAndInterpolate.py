import vanilla
import os
from AppKit import *
from mojo.events import addObserver, removeObserver
from mojo.UI import GetFile


"""
Scale and Interpolate glyphs
2020_02_03 Andy Clymer
"""
VERSION = "v1.5"


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


def interpolateAndScaleGuides(CASEINFO, obj0, obj1, destObj):
    # Interpolate and scale guides that share names, and set them to a destination object
    obj0guides = {}
    for g0 in obj0.guidelines:
        if g0.name:
            if not g0.name in obj0guides:
                obj0guides[g0.name] = g0
    for g1 in obj1.guidelines:
        if g1.name:
            if g1.name in obj0guides:
                g0 = obj0guides[g1.name]
                # x (interpolate and scale)
                x = interpolate(CASEINFO["interpH"], getattr(g0, "x"), getattr(g1, "x"))
                x *= CASEINFO["scaleH"]
                # y (interpolate and scale)
                y = interpolate(CASEINFO["interpV"], getattr(g0, "y"), getattr(g1, "y"))
                y *= CASEINFO["scaleV"]
                # angle, name, color (copy)
                angle = g0.angle
                name = g0.name
                color = g0.color
                # Append
                destObj.appendGuideline(position=(x, y), angle=angle, name=name, color=color)


def getFontName(font, fonts):
    # A helper to get the font name, starting with the preferred name and working back to the PostScript name
    # Make sure that it's not the same name as another font in the fonts list
    if font.info.openTypeNamePreferredFamilyName and font.info.openTypeNamePreferredSubfamilyName:
        name = "%s %s" % (font.info.openTypeNamePreferredFamilyName, font.info.openTypeNamePreferredSubfamilyName)
    elif font.info.familyName and font.info.styleName:
        name = "%s %s" % (font.info.familyName, font.info.styleName)
    elif font.info.fullName:
        name = font.info.fullName
    elif font.info.fullName:
        name = font.info.postscriptFontName
    else: name = "Untitled"
    # Add a number to the name if this name already exists
    if name in fonts:
        i = 2
        while name + " (%s)" % i in fonts:
            i += 1
        name = name + " (%s)" % i
    return name
    

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
    #fontName = f.info.postscriptFontName
    fontName = getFontName(f, AllFonts())
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
        
        self.w = vanilla.Window((317, 700), "Scale And Interpolate %s" % VERSION, minSize=(317, 300), maxSize=(317, 969), autosaveName="ScaleAndInterp") # 882 height
        
        self.g = vanilla.Group((0, 0, 300, 900))
        
        step = 10
        self.g.font0title = vanilla.TextBox((10, step, -10, 25), colorText("Lightest Master (0%)", style="bold"))
        self.g.font0choice = vanilla.PopUpButton((10, step+20, -10, 25), self.fontNames, callback=self.fontChoiceChanged)
        step += 50
        self.g.font0stemTextUC = vanilla.TextBox((20, step, -10, 20), "")
        self.g.font0stemTextLC = vanilla.TextBox((20, step+20, -10, 20), "")
        step += 50
        self.g.font1title = vanilla.TextBox((10, step, -10, 25), colorText("Heaviest Master (100%)", style="bold"))
        self.g.font1choice = vanilla.PopUpButton((10, step+20, -10, 25), self.fontNames, callback=self.fontChoiceChanged)
        step += 50
        self.g.font1stemTextUC = vanilla.TextBox((20, step, -10, 20), "")
        self.g.font1stemTextLC = vanilla.TextBox((20, step+20, -10, 20), "")
        step += 50
        
        self.g.hr1 = vanilla.HorizontalLine((10, step, -10, 1))
        
        step += 15
        self.g.capsTitle = vanilla.TextBox((10, step, -10, 25), colorText("Caps", style="bold"))
        step += 25
        self.g.ucGroups = vanilla.PopUpButton((10, step, -10, 25), [])
        step += 35
        columnDescriptions = [dict(title="Name"), dict(title="Value", editable=True, width=50)]
        capInfo = [
            dict(Name="Scale Horizontal %", attr="scaleH", Value=100),
            dict(Name="Scale Vertical %", attr="scaleV", Value=100),
            dict(Name="Interpolate Horizontal %", attr="interpH", Value=100),
            dict(Name="Interpolate Vertical %", attr="interpV", Value=100),
            dict(Name="Units of tracking", attr="tracking", Value=0)]
        self.g.ucInfo = vanilla.List((10, step, -10, 100), capInfo, columnDescriptions=columnDescriptions, showColumnTitles=False, editCallback=self.dataChanged)
        step += 110
        self.g.resultStemTextUC = vanilla.TextBox((20, step, -10, 20), "")
        step += 30
        
        self.g.lcTitle = vanilla.TextBox((10, step, -10, 25), colorText("Lowercase", style="bold"))
        step += 25
        self.g.lcGroups = vanilla.PopUpButton((10, step, -10, 25), [])
        step += 35
        lcInfo = [
            dict(Name="Scale Horizontal %", attr="scaleH", Value=100),
            dict(Name="Scale Vertical %", attr="scaleV", Value=100),
            dict(Name="Interpolate Horizontal %", attr="interpH", Value=100),
            dict(Name="Interpolate Vertical %", attr="interpV", Value=100),
            dict(Name="Units of tracking", attr="tracking", Value=0)]
        self.g.lcInfo = vanilla.List((10, step, -10, 100), lcInfo, columnDescriptions=columnDescriptions, showColumnTitles=False, editCallback=self.dataChanged)
        step += 110
        self.g.resultStemTextLC = vanilla.TextBox((20, step, -10, 20), "")
        step += 30
        
        self.g.otherTitle = vanilla.TextBox((10, step, -10, 25), colorText("Other glyphs", style="bold"))
        step += 25
        self.g.otherRadio = vanilla.RadioGroup((10, step, -10, 70), 
            ["Copy from the lightest master", 
            "Process at 50% of UC and LC settings", 
            "Skip any other glyphs"], callback=self.dataChanged)
        self.g.otherRadio.set(2)
        
        step += 80
        
        self.g.loadButton = vanilla.SquareButton((100, step, -10, 25), "Load settings from UFO", callback=self.loadSettings)
        step += 35
        
        self.g.hr2 = vanilla.HorizontalLine((10, step, -10, 1))
        step += 15
        self.g.skewBox = vanilla.CheckBox((10, step, -10, 25), "Skew Italic glyphs upright before scaling")
        self.g.skewBox.set(True)
        step += 25
        self.g.infoBox = vanilla.CheckBox((10, step, -10, 25), "Interpolate Font Info whenever possible")
        self.g.infoBox.set(True)
        step += 25
        self.g.scaleComponentBox = vanilla.CheckBox((10, step, -10, 25), "Don’t scale component positions")
        self.g.scaleComponentBox.set(True)
        step += 25
        self.g.doKernBox = vanilla.CheckBox((10, step, -10, 25), "Process Kerning")
        self.g.doKernBox.set(True)
        step += 3
        self.g.testKernButton = vanilla.SquareButton((135, step, -10, 25), "Compatibility Test", callback=self.kernCompatibilityTestCallback)
    
        #step += 40
        self.w.buildButton = vanilla.SquareButton((10, -35, -10, 25), "Make Font", callback=self.makeFontCallback)
        
        # Add the group to a ScrollView
        view = self.g.getNSView()
        self.w.sv = vanilla.ScrollView((0, 0, -0, -45), view, hasHorizontalScroller=False, hasVerticalScroller=True, autohidesScrollers=False, drawsBackground=False)#backgroundColor=NSColor.windowBackgroundColor())
        
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
        font0choice = self.g.font0choice.get()
        if font0choice >= 0: font0choice = self.fontNames[font0choice]
        font1choice = self.g.font1choice.get()
        if font1choice >= 0: font1choice = self.fontNames[font1choice]
        ucGroupsChoice = self.g.ucGroups.get()
        if ucGroupsChoice >= 0: ucGroupsChoice = self.g.ucGroups.getItems()[ucGroupsChoice]
        lcGroupsChoice = self.g.lcGroups.get()
        if lcGroupsChoice >= 0: lcGroupsChoice = self.g.lcGroups.getItems()[lcGroupsChoice]
                
        # Collect font info
        self.fontNames = []
        self.fontList = []
        self.fontStems = []
        fonts = AllFonts()
        for f in AllFonts():
            #name = f.info.postscriptFontName
            name = getFontName(f, fonts)
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
        self.g.font0choice.setItems(self.fontNames)
        if font0choice in self.fontNames:
            idx = self.fontNames.index(font0choice)
        else: idx = 0
        self.g.font0choice.set(idx)
        # Font1
        self.g.font1choice.setItems(self.fontNames)
        if font1choice in self.fontNames:
            idx = self.fontNames.index(font1choice)
        else: idx = 0
        self.g.font1choice.set(idx)
        # ucGroups
        self.g.ucGroups.setItems(groupNames)
        if ucGroupsChoice in groupNames:
            idx = groupNames.index(ucGroupsChoice)
        else: idx = 0
        self.g.ucGroups.set(idx)
        # lcGroups
        self.g.lcGroups.setItems(groupNames)
        if lcGroupsChoice in groupNames:
            idx = groupNames.index(lcGroupsChoice)
        else: idx = 0
        self.g.lcGroups.set(idx)
                
        # And update other font settings
        self.dataChanged()
    

    def fontChoiceChanged(self, sender=None):
        # Font choice changed
        font0Idx = self.g.font0choice.get()
        font1Idx = self.g.font1choice.get()
        
        # Update the stem measurement
        self.estimateStems()
        
        # Reset the stem descriptions
        self.g.font0stemTextUC.set(colorText("UC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.g.font0stemTextLC.set(colorText("LC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.g.font1stemTextUC.set(colorText("UC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.g.font1stemTextLC.set(colorText("LC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.g.resultStemTextUC.set(colorText("UC stems: (Uncertain)", color="gray", sizeStyle="small"))
        self.g.resultStemTextLC.set(colorText("LC stems: (Uncertain)", color="gray", sizeStyle="small"))
        
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
                        self.g.font0stemTextUC.set(stemsText[0])
                        self.g.font0stemTextLC.set(stemsText[1])
                    else:
                        self.g.font1stemTextUC.set(stemsText[0])
                        self.g.font1stemTextLC.set(stemsText[1])
                    
            # Updated estimated stem descriptions
            if not self.estimatedStems == None:
                for case in ["uc", "lc"]:
                    stems = self.estimatedStems[case]
                    if stems:
                        stemText = "%s stems: " % case.upper()
                        stemText += "%s horizontal, %s vertical" % (stems["horiz"], stems["vert"])
                        if case == "uc":
                            self.g.resultStemTextUC.set(colorText(stemText, color="gray", sizeStyle="small"))
                        else: self.g.resultStemTextLC.set(colorText(stemText, color="gray", sizeStyle="small"))


    
    def dataChanged(self, sender=None):
        # Data settings changed, normalize it all and hold it aside
        
        self.normalizedInfo = dict(uc=dict(problem=False), lc=dict(problem=False), other=dict(problem=False))
        
        # Run through the cases
        for case in ["uc", "lc"]:
            # Collect data
            if case == "uc":
                INFOLIST = self.g.ucInfo
            else: INFOLIST = self.g.lcInfo
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
        otherChoice = self.g.otherRadio.get()
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
            font0Idx = self.g.font0choice.get()
            font1Idx = self.g.font1choice.get()
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
                self.g.otherRadio.set(libData["otherOption"])
                self.g.skewBox.set(libData["skewOption"])
                self.g.infoBox.set(libData["infoOption"])
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
                        self.g.ucInfo.set(info)
                    else: self.g.lcInfo.set(info)
                # Reset the dropdown choices
                self.g.font0choice.set(-1)
                self.g.font1choice.set(-1)
                self.g.ucGroups.set(0)
                self.g.lcGroups.set(0)
        
            prevFont.close()
        
        
        
    def makeFontCallback(self, sender):
        # Validate data
        ready = True
        font0Idx = self.g.font0choice.get()
        font1Idx = self.g.font1choice.get()
        if not -1 in [font0Idx, font1Idx]:
            if font0Idx == font1Idx:
                ready = False
                print("Choose two different fonts")
        else:
            ready = False
            print("Choose two fonts")
        # Groups
        group0Idx = self.g.ucGroups.get()
        group1Idx = self.g.lcGroups.get()
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
        font0Idx = self.g.font0choice.get()
        font1Idx = self.g.font1choice.get()
        font0 = self.fontList[font0Idx]
        font1 = self.fontList[font1Idx]
        destFont = NewFont(showInterface=False)
        
        # Fetch the charsets
        groupChoiceIdxUC = self.g.ucGroups.get()
        groupChoiceIdxLC = self.g.lcGroups.get()
        charsetUC = self.groups[groupChoiceIdxUC]["glyphNames"]
        charsetLC = self.groups[groupChoiceIdxLC]["glyphNames"]
        # Collect an "other" charset
        charsetOther = []
        if not self.g.otherRadio.get() == 2: # 2 = Skip
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
                    if self.g.skewBox.get():
                        angle0 = font0.info.italicAngle
                        if not angle0: angle0 = 0
                        g0.skewBy(angle0)
                        angle1 = font1.info.italicAngle
                        if not angle1: angle1 = 0
                        g1.skewBy(angle1)
                        # ...but skew back the components to be upright if the components aren't scaling
                        if self.g.scaleComponentBox.get():
                            for c in g0.components:
                                c.skewBy(-angle0)
                            for c in g1.components:
                                c.skewBy(-angle1)
                    
                    # Interpolate
                    destGlyph = destFont.newGlyph(gName)
                    destGlyph = destFont[gName]
                    destGlyph.interpolate((CASEINFO["interpH"], CASEINFO["interpV"]), g0, g1)
                    
                    # Hold aside component scale
                    compScales = []
                    if self.g.scaleComponentBox.get():
                        for c in destGlyph.components:
                            compScales.append(c.scale)
                    
                    # Scale
                    destGlyph.scaleBy((CASEINFO["scaleH"], CASEINFO["scaleV"]))
                    destGlyph.width = int(round(destGlyph.width * CASEINFO["scaleH"]))
                    
                    # Interpolate the Italic Angle and skew back
                    if self.g.skewBox.get():
                        if not (angle0, angle1) == (0, 0):
                            f = (CASEINFO["interpH"] + CASEINFO["interpV"]) * 0.5
                            interpAngle = interpolate(f, angle0, angle1)
                            destGlyph.skewBy(-interpAngle)
                            # ...but reset the components if we're not skewing/scaling them
                            if self.g.scaleComponentBox.get():
                                for c in destGlyph.components:
                                    c.skewBy(interpAngle)
                                    # ...and fix it if it's now off by a tiny rounding error
                                    if 0.0001 > c.transformation[2] > -0.0001:
                                        t = list(c.transformation)
                                        t[2] = 0
                                        c.transformation = t
                    
                    # Track
                    if destGlyph.leftMargin:
                        destGlyph.leftMargin += int(round(CASEINFO["tracking"]*0.5))
                        destGlyph.rightMargin += int(round(CASEINFO["tracking"]*0.5))
                    else: destGlyph.width += CASEINFO["tracking"]
                
                    # Set component scale back to where it was
                    if self.g.scaleComponentBox.get():
                        for cIdx, s in enumerate(compScales):
                            destGlyph.components[cIdx].scale = s
                            
                    # Unicodes
                    if g0.unicodes == g1.unicodes:
                        destGlyph.unicodes = g0.unicodes
                    
                    # Done
                    destGlyph.markColor = None
                    destGlyph.changed()
        
        # Process kerning
        if self.g.doKernBox.get():
            groupTestResult = self.kernCompatibilityTest()
            if not groupTestResult["report"]:
                # The kerning groups are compatible, can continue with the kerning
                destFont.groups.update(font0.groups)
                kernDict = self.doProcessKerns()
                destFont.kerning.update(kernDict)
            else:
                # Groups are incompatible, print the test result
                self.kernCompatibilityTestCallback(None)
        
        # Font Guides (use the "other" set)
        interpolateAndScaleGuides(self.normalizedInfo["other"], font0, font1, destFont)
        
        # Start the Font Info
        # ...and interpolate/scale a few values
        copyAttrs = ["familyName", "unitsPerEm"]
        if self.g.infoBox.get():
            # Copy some attributes
            for attr in copyAttrs:
                setattr(destFont.info, attr, getattr(font0.info, attr))
            # Interpolate and scale other attributes
            if not None in [font0.info.capHeight, font1.info.capHeight]:
                capHeight = interpolate(self.normalizedInfo["uc"]["interpV"], font0.info.capHeight, font1.info.capHeight)
                capHeight *= self.normalizedInfo["uc"]["scaleV"]
                destFont.info.capHeight = capHeight
            if not None in [font0.info.xHeight, font1.info.xHeight]:
                xHeight = interpolate(self.normalizedInfo["lc"]["interpV"], font0.info.xHeight, font1.info.xHeight)
                xHeight *= self.normalizedInfo["lc"]["scaleV"]
                destFont.info.xHeight = xHeight
            if not None in [font0.info.ascender, font1.info.ascender]:
                ascender = interpolate(self.normalizedInfo["lc"]["interpV"], font0.info.ascender, font1.info.ascender)
                ascender *= self.normalizedInfo["lc"]["scaleV"]
                destFont.info.ascender = ascender
            if not None in [font0.info.descender, font1.info.descender]:
                descender = interpolate(self.normalizedInfo["lc"]["interpV"], font0.info.descender, font1.info.descender)
                descender *= self.normalizedInfo["lc"]["scaleV"]
                destFont.info.descender = descender
            if not None in [font0.info.italicAngle, font1.info.italicAngle]:
                italicAngle = interpolate(self.normalizedInfo["lc"]["interpH"], font0.info.italicAngle, font1.info.italicAngle)
                destFont.info.italicAngle = italicAngle
            
        # Save the settings to the font.lib
        libData = dict(
            normalizedInfo=self.normalizedInfo,
            otherOption=self.g.otherRadio.get(),
            skewOption=self.g.skewBox.get(),
            infoOption=self.g.infoBox.get())
        destFont.lib[LIBKEY] = libData

        # Finish and open the font
        destFont.glyphOrder = font0.glyphOrder
        
        destFont.changed()
        destFont.openInterface()
        
        
    def kernCompatibilityTestCallback(self, sender):
        # Print a compatibility test
        if len(self.fontList) > 1:
            groupTestResult = self.kernCompatibilityTest()
            print("-"*30)
            print("Kerning group report:")
            if not groupTestResult["report"]:
                print("\tAll OK!")
            else: print(groupTestResult["report"])
            print("-"*30)
        
    
    def doProcessKerns(self):
        groupTestResult = self.kernCompatibilityTest()
        if not groupTestResult["report"]:
            # The groups match, kern processing can continue

            font0Idx = self.g.font0choice.get()
            font1Idx = self.g.font1choice.get()
            font0 = self.fontList[font0Idx]
            font1 = self.fontList[font1Idx]
            
            # Group all kernable items (group names and glyph names) by their classifications
            kernItemsByClass = dict(uc=[], lc=[], other=[])
            kernItemsByClass["uc"] += groupTestResult["charsetUC"]
            kernItemsByClass["uc"] += groupTestResult["groupsUC"]
            kernItemsByClass["lc"] += groupTestResult["charsetLC"]
            kernItemsByClass["lc"] += groupTestResult["groupsLC"]
            kernItemsByClass["other"] += groupTestResult["charsetOther"]
            kernItemsByClass["other"] += groupTestResult["groupsOther"]
            # Make a quick reverse lookup of this dict
            kernItemClasses = {}
            for c in kernItemsByClass:
                for i in kernItemsByClass[c]:
                    kernItemClasses[i] = c
                    
            # Collect all kerning pairs, from both masters
            pairs = []
            for f in [font0, font1]:
                for pair in f.kerning.keys():
                    if not pair in pairs:
                        pairs.append(pair)
                        
            # Go one-by-one through all the pairs and scale/interpolate the values
            newKernDict = {}
            for pair in pairs:
                if not False in [pair[0] in kernItemClasses, pair[1] in kernItemClasses]:
                    # Get the value from each font
                    value0 = font0.kerning.get(pair, 0)
                    value1 = font1.kerning.get(pair, 0)
                    # Find the item classifications
                    classL = kernItemClasses[pair[0]]
                    classR = kernItemClasses[pair[1]]
                    # Process the left class first
                    v = interpolate(self.normalizedInfo[classL]["interpH"], value0, value1)
                    v = v * self.normalizedInfo[classL]["scaleH"]
                    # If the L and R classes differ, process again and take the 50% avg
                    if not classL == classR:
                        vR = interpolate(self.normalizedInfo[classR]["interpH"], value0, value1)
                        vR = vR * self.normalizedInfo[classR]["scaleH"]
                        v = interpolate(0.5, v, vR)
                    newKernDict[pair] = v
            
            return newKernDict
                    
        
    
    def kernCompatibilityTest(self):
        # Test the kerning for compatibility
        # Kerning groups must be identical between masters
        # Chosen UC and LC groups must not conflict with the group contents (i.e. no mixing UC and LC in the same group)
        # Give a report for group compatibility
        
        font0Idx = self.g.font0choice.get()
        font1Idx = self.g.font1choice.get()
        font0 = self.fontList[font0Idx]
        font1 = self.fontList[font1Idx]
        font0name = self.g.font0choice.getItems()[font0Idx]
        font1name = self.g.font1choice.getItems()[font1Idx]
        
        # Build a report for the problems
        groupReport = []
        # Be ready to sort the kerning groups by classification
        groupsUC = []
        groupsLC = []
        groupsOther = []
        charsetUC = []
        charsetLC = []
        charsetOther = []
        
        # Fetch the charsets
        groupChoiceIdxUC = self.g.ucGroups.get()
        groupChoiceIdxLC = self.g.lcGroups.get()
        if 0 in [groupChoiceIdxUC, groupChoiceIdxLC]:
            groupReport.append("\tProblem: Choose two different groups or two different fonts")

        else:
            charsetUC = self.groups[groupChoiceIdxUC]["glyphNames"]
            charsetLC = self.groups[groupChoiceIdxLC]["glyphNames"]
            # Collect an "other" charset
            charsetOther = []
            if not self.g.otherRadio.get() == 2: # 2 = Skip
                for gn in font0.keys():
                    if gn in font1.keys():
                        if not True in [gn in charsetUC, gn in charsetLC]:
                            charsetOther.append(gn)
        
            # Group contents
            for group0name in font0.groups.keys():
                if group0name.startswith("public.kern"):
                    if not group0name in font1.groups:
                        groupReport.append("\tMissing kerning group:   %s is not in %s" % (group0name, font1name))
                    else:
                        # Test if contents match
                        if not font0.groups[group0name] == font1.groups[group0name]:
                            groupReport.append("\tMismatching glyph list:  %s" % group0name)
                        else:
                            # Test if contents are in matching classifications
                            classifications = dict(uc=[], lc=[], etc=[])
                            for gn in font0.groups[group0name]:
                                if gn in charsetUC:
                                    classifications["uc"].append(gn)
                                elif gn in charsetLC:
                                    classifications["lc"].append(gn)
                                else: classifications["etc"].append(gn)
                            # Report if the classifications are mixed
                            classifications = [c[0] for c in classifications.items() if not len(c[1]) == 0]
                            if len(classifications) > 1:
                                classReport = ""
                                for c in ["uc", "lc", "etc"]:
                                    names = classifications[c]
                                    if len(names):
                                        #if len(classReport): classReport += ", "
                                        classReport += "(%s: %s) " % (c.upper(), " ".join(classifications[c]))
                                groupReport.append("\tIncompatible group:      %s %s" % (group0name, classReport))
                            else:
                                # The group is ok! It's the same in both fonts and all the glyphs are in the same classification
                                c = classifications[0]
                                if c == "uc":
                                    groupsUC.append(group0name)
                                elif c == "lc":
                                    groupsLC.append(group0name)
                                else: groupsOther.append(group0name)
            # One more test from font1 to font0 for missing groups
            for group1name in font1.groups.keys():
                if group1name.startswith("public.kern"):
                    if not group1name in font0.groups:
                        groupReport.append("\tMissing kerning group:   %s is not in %s" % (group1name, font0name))
                    
        groupReport.sort()
        if len(groupReport):
            fullReport = "\n".join(groupReport)
        else: fullReport = None
        return dict(
            groupsUC=groupsUC, 
            groupsLC=groupsLC, 
            groupsOther=groupsOther, 
            charsetUC=charsetUC,
            charsetLC=charsetLC,
            charsetOther=charsetOther,
            report=fullReport)
        
        
        

ScaleAndAdjust()