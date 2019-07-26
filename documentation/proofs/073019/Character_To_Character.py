import datetime

now = datetime.datetime.now()
newFileName = "spacingstrings" + now.strftime("%Y_%m_%d-%H_%M_%S")

# Text from external source
path = "chars_to_chars.txt"
textstuff = open(path, "r", encoding="utf-8")
textread = textstuff.read()
textstuff.close()

# Variables
fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
frauncesVals = listFontVariations(fnames[0])
wghtMin = frauncesVals['wght']['minValue']
wghtMax = frauncesVals['wght']['maxValue']
opMin = frauncesVals['opsz']['minValue']
opMax = frauncesVals['opsz']['maxValue']

wghtVals = (wghtMin, wghtMax)
opVals = (opMin, opMax)

margin = 50
gutter = 25
columns = (4,2)
sizeincrements = 72
masters = len(wghtVals) + len(opVals)
fSize = 72

for f in range(0,2,1):
    for x in range(0,len(opVals),1):
        newPage("TabloidLandscape")
        textread1 = textread
        for y in range(0,len(wghtVals),1):
            font(fnames[f], fSize)
            fontVariations(opsz=x,wght=y)
            while len(textread1) > 0:
                textread1 = textBox(textread1, (margin,margin+height()/4*y,width()-margin*2,height()/4), align="center")
        