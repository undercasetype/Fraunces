import vanilla
import os


"""
Scale and Adjust glyphs
2019_09_18 Andy Clymer

v1

"""

CHARSET_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ&?¿!¡.,0123456789"
CHARSET_LOWER = "abcdefghijklmnopqrstuvwxyz"

class ScaleAndAdjust:
    
    def __init__(self):
        
        self.fontList = []
        self.fontNames = []
        for f in AllFonts():
            name = str(f.info.postscriptFontName)
            if not name in self.fontNames:
                self.fontNames.append(name)
                self.fontList.append(f)
        
        self.w = vanilla.Window((300, 500), "Scale And Adjust")
        step = 10
        self.w.font0title = vanilla.TextBox((10, step, -10, 25), "Lightest Weight (0%)")
        self.w.font0choice = vanilla.PopUpButton((10, step+20, -10, 25), self.fontNames)
        step += 60
        self.w.font1title = vanilla.TextBox((10, step, -10, 25), "Heaviest Weight (100%)")
        self.w.font1choice = vanilla.PopUpButton((10, step+20, -10, 25), self.fontNames)
        
        step += 60
        self.w.hr1 = vanilla.HorizontalLine((10, step, -10, 1))
        step += 10
        self.w.capsTitle = vanilla.TextBox((10, step, -10, 25), "Caps")
        
        step += 30
        
        columnDescriptions = [dict(title="Name"), dict(title="Value", editable=True, width=50)]
        capInfo = [
            dict(Name="Scale Horizontal %", Value=100),
            dict(Name="Scale Vertical %", Value=100),
            dict(Name="Interpolate Horizontal %", Value=100),
            dict(Name="Interpolate Vertical %", Value=100),
            dict(Name="Units of tracking", Value=0)]
        self.w.ucInfo = vanilla.List((10, step, -10, 100), capInfo, columnDescriptions=columnDescriptions, showColumnTitles=False)
        
        step += 120
        
        self.w.lcTitle = vanilla.TextBox((10, step, -10, 25), "Lowercase")
        step += 30
        lcInfo = [
            dict(Name="Scale Horizontal %", Value=100),
            dict(Name="Scale Vertical %", Value=100),
            dict(Name="Interpolate Horizontal %", Value=100),
            dict(Name="Interpolate Vertical %", Value=100),
            dict(Name="Units of tracking", Value=0)]
        self.w.lcInfo = vanilla.List((10, step, -10, 100), lcInfo, columnDescriptions=columnDescriptions, showColumnTitles=False)
        
        step += 120
        self.w.hr2 = vanilla.HorizontalLine((10, step, -10, 1))
        step += 20
        self.w.buildButton = vanilla.SquareButton((10, step, -10, 25), "Make Font", callback=self.makeFontCallback)
        
        self.w.open()
        
        
    def makeFontCallback(self, sender):
        # Validate data
        font0Idx = self.w.font0choice.get()
        font1Idx = self.w.font1choice.get()
        #lcInfo = self.w.lcInfo.get()
        #ucInfo = self.w.ucInfo.get()
        if not -1 in [font0Idx, font1Idx]:
            if not font0Idx == font1Idx:
                self.doMakeFont()
            else: print("Choose two different fonts")
        else: print("Select two fonts")
    
    def doMakeFont(self):
        # Make a new font
        font0Idx = self.w.font0choice.get()
        font1Idx = self.w.font1choice.get()
        font0 = self.fontList[font0Idx]
        font1 = self.fontList[font1Idx]
        destFont = NewFont()
        
        # Font info
        destFont.info.unitsPerEm = font0.info.unitsPerEm
        
        charMap = font0.getCharacterMapping()
        
        # Run through the cases
        for case in ["UC", "LC"]:
            
            # Collect data
            if case == "UC":
                CHARSET = CHARSET_CAPS
                INFO = self.w.ucInfo.get()
            else:
                CHARSET = CHARSET_LOWER
                INFO = self.w.lcInfo.get()
            
            interpH = 1
            interpV = 1
            scaleH = 1
            scaleV = 1
            tracking = 0
            # Clean up the data
            for item in INFO:
                if item["Name"] == "Scale Horizontal %":
                    try:
                        scaleH = float(item["Value"]) * 0.01
                    except:
                        print("Problem with a 'Scale Horizontal %' value")
                        scaleH = 1
                elif item["Name"] == "Scale Vertical %":
                    try:
                        scaleV = float(item["Value"]) * 0.01
                    except:
                        print("Problem with a 'Scale Vertical %' value")
                        scaleV = 1
                elif item["Name"] == "Interpolate Horizontal %":
                    try:
                        interpH = float(item["Value"]) * 0.01
                    except:
                        print("Problem with a 'Interpolate Horizontal %' value")
                        interpH = 1
                elif item["Name"] == "Interpolate Vertical %":
                    try:
                        interpV = float(item["Value"]) * 0.01
                    except:
                        print("Problem with a 'Interpolate Vertical %' value")
                        interpV = 1
                elif item["Name"] == "Units of tracking":
                    try:
                        tracking = float(item["Value"])
                    except:
                        print("Problem with a 'Units of tracking' value")
                        tracking = 1
            
            
            # Process the glyphs
            for character in CHARSET:
                gName = charMap.get(ord(character))
                if gName:
                    gName = gName[0]
                    if gName in font0 and gName in font1:
                        
                        # Interpolate
                        destGlyph = destFont.newGlyph(gName)
                        destGlyph = destFont[gName]
                        g0 = font0[gName]
                        g1 = font1[gName]
                        destGlyph.interpolate((interpH, interpV), g0, g1)
                        
                        # Scale
                        destGlyph.scaleBy((scaleH, scaleV))
                        destGlyph.width = int(round(destGlyph.width * scaleH))
                        
                        # Track
                        destGlyph.leftMargin += int(round(tracking*0.5))
                        destGlyph.rightMargin += int(round(tracking*0.5))
                        
                        # Done
                        destGlyph.changed()



ScaleAndAdjust()