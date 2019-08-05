import datetime

now = datetime.datetime.now()
newFileName = "character_to_character" + now.strftime("%Y_%m_%d-%H_%M_%S")

# Text from external source
path = "chars_to_chars.txt"
textstuff = open(path, "r", encoding="utf-8")
textread = textstuff.read()
textstuff.close()
# textread = textread.split("\n")
# textread = textread[1]

# Variables
fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
frauncesVals = listFontVariations(fnames[0])
wghtMin = frauncesVals['wght']['minValue']
wghtMax = frauncesVals['wght']['maxValue']
opMin = frauncesVals['opsz']['minValue']+0.1
opMax = frauncesVals['opsz']['maxValue']

wghtVals = (wghtMin, wghtMax)
opVals = (opMin, opMax)

margin = 50
gutter = 25
columns = (4,2)
rows = 3
masters = len(wghtVals) + len(opVals)
fSize = 72
captionHeight = 24
boxHeight = ((height()-(margin*2))/(rows)) - (gutter*(rows-1)) - captionHeight

pages = 3
opSzsteps = (opMax-opMin) / (pages-1)
wghtSteps = (wghtMax-wghtMin) / (rows-1)

# Roman and Italic
for f in range(0,2,1):
    # Steps for opsz
    for x in range(0,pages,1):
        newPage("TabloidLandscape")
        # Steps for wght
        for y in range(0,rows,1):
            font(fnames[f], fSize)
            opSz = opMin+(opSzsteps*y)
            wgHt = wghtMin+(wghtSteps*x)
            fontVariations(opsz = opSz,wght = wgHt)
            textBox(textread, (margin,margin+(boxHeight*y),width()-margin*2,boxHeight), align = "center")
            font(fnames[2],9)
            textBox("OpSz: %s, Wght: %s" % (opSz,wgHt), (margin,margin+(boxHeight*y)-boxHeight+captionHeight,width()-margin*2,boxHeight), align = "center")
            
# Old to New Comparison

fontdict = {"Fraunces Beta Regular OpMin": (9.1,400), "Fraunces Beta Bold OpMin": (9.1,750), "Fraunces Beta Regular OpMax": (144,400), "Fraunces Italic Beta Regular OpMin": (9.1,400), "Fraunces Italic Beta Bold OpMin": (9.1,750), "Fraunces Italic Beta Regular OpMax": (144,400), }

def drawOldtoNewComparison(style):
    newPage("TabloidLandscape")
    font(style, fSize)
    textBox(textread,(margin,margin, width()-(margin*2),boxHeight),align = "center")
    font(fnames[2],9)
    tracking(None)
    textBox(style, (margin,margin-boxHeight+captionHeight,width()-margin*2,boxHeight), align = "center")
    if "Fraunces Italic" in style:
        font("Fraunces Italic", fSize)
    else:
        font("Fraunces", fSize)
    fontVariations(opsz = fontdict[style][0], wght = fontdict[style][1])
    textBox(textread,(margin,margin+(boxHeight*y), width()-(margin*2),boxHeight),align = "center")
    font(fnames[2],9)
    textBox("Fraunces %s" % (str(fontdict[style])), (margin,300,width()-margin*2,boxHeight), align = "center")
    
drawOldtoNewComparison("Fraunces Beta Regular OpMin")
drawOldtoNewComparison("Fraunces Beta Bold OpMin")
drawOldtoNewComparison("Fraunces Beta Regular OpMax")
drawOldtoNewComparison("Fraunces Italic Beta Regular OpMin")
drawOldtoNewComparison("Fraunces Italic Beta Bold OpMin")
drawOldtoNewComparison("Fraunces Italic Beta Regular OpMax")
    
            
saveImage("PDFs/%s.pdf" % (newFileName))
        