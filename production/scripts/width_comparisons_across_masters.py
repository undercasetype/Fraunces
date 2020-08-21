# Phaedra Charles 04-28-2020

# Script to generate comparisons across multiple masters, showing rates of 
# change in width for every glyph. Any glyph that falls outside of an average "meanTotals" 
# is flagged as possibly expanding or contracting at an undesirable rate.

# Script is executed by running "glyphReport()" function, with "filterSensitivity" a percentage of change.
# Script can only compare a master against another master. Future version could include comparisons
# across multiple masters.

from vanilla.dialogs import *

meanTotals = {}

# How do I specify the fontBase, and fontCompare?

def glyphReport(filterSensitivity):
    
    baseFontPath = getFile("Select font as base for comparison:", allowsMultipleSelection=False, fileTypes=["ufo"])[0]
    compFontPath = getFile("Select font to be used as comparison:", allowsMultipleSelection=False, fileTypes=["ufo"])[0]
    baseFont = OpenFont(baseFontPath, showInterface = False)
    compFont = OpenFont(compFontPath, showInterface = False)
    
    fonts = (baseFont, compFont)
    glyphdict = {}

    for font in fonts:
        for glyph in font:
            #print(glyph)
            if glyph.markColor != None:
                glyphWidth = glyph.width-(glyph.leftMargin+glyph.rightMargin)
                glyphdict.setdefault(glyph.name, [])
                glyphdict[glyph.name].append(glyphWidth)

    for i in glyphdict.copy():
        if len(glyphdict[i]) < 2:
            glyphdict.pop(i)

    for entry in glyphdict:
        percent = int((glyphdict[entry][0]/glyphdict[entry][1])*100)
        glyphdict[entry] = percent

    meanTotal = 0
    
    for key, value in glyphdict.items():
        meanTotal += value
    
    meanTotal = int(meanTotal/len(glyphdict))
    meanTotals[str(fonts[0].info.familyName + " " + fonts[0].info.styleName)+" to "+str(fonts[1].info.familyName + " " + fonts[1].info.styleName)] = meanTotal

    outliers = []

    for key, value in sorted(glyphdict.items(), key = lambda item: item[1]):
        difference = value-meanTotal
        if difference <= -filterSensitivity or difference >= filterSensitivity:
            outliers.append("%s: %s%%" % (key, value-meanTotal))

    print("Glyph-to-glyph comparison between %s and %s with a filterSensitivity of +-%s:" % (
        (fonts[0].info.familyName + " " + fonts[0].info.styleName), 
        (fonts[1].info.familyName + " " + fonts[1].info.styleName), filterSensitivity))
    print(outliers)
    
glyphReport(5)
glyphReport(5)
glyphReport(5)
glyphReport(5)

print(meanTotals)