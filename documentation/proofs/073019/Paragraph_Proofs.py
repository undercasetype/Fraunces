import datetime

now = datetime.datetime.now()
newFileName = "paragraph_proofs" + now.strftime("%Y_%m_%d-%H_%M_%S")

fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
frauncesVals = listFontVariations(fnames[0])
wghtMin = frauncesVals['wght']['minValue']
wghtMax = frauncesVals['wght']['maxValue']
opMin = frauncesVals['opsz']['minValue'] + 0.1
opMax = frauncesVals['opsz']['maxValue']

# Text from external source
# path = "sampletext.txt"
# textstuff = open(path, "r", encoding="utf-8")
# textsample = textstuff.read()
# textstuff.close()

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10
pLength = 200

#textsample = textsample.split(" ")

# This function generates formatted strings by randomly picking from the two fonts list, using the size specified, and paragraph length specified.

def textGenerator(fSize, pLength, fontpick=None, track=None, isUpper=None):
    path = "sampletext.txt"
    textstuff = open(path, "r", encoding="utf-8")
    textsample = textstuff.read()
    textstuff.close()
    if isUpper == True:
        textsample = textsample.upper()
    textsample = textsample.split(" ")
    text = FormattedString()
    for x in range(0, pLength, 1):    
        text.fontVariations(opsz = fSize , wght = (100*y) + 100 )
        if fontpick in fnames:
            text.append(choice(textsample) + " ", font = fnames[fnames.index(fontpick)], fontSize = fSize, fill = 0)
        elif fontpick == None:
            text.append(choice(textsample) + " ", font = choice(fnames[0:2]), fontSize = fSize, fill = 0)
    return text
    
## Lowercase Paragraph Settings

for y in range(0,pages,1):
    # textsamplenew = ""
    # for x in range(0,100,1):
    #     textsamplenew += choice(textsample) + " "
    newPage("TabloidLandscape")
    pageHeight = height()-(margin*2)
    boxMargin = (margin/2)
    boxWidth = (width()/2)- boxMargin
    topBoxHeight = (pageHeight/1.5) - boxMargin
    bottomBoxHeight = (pageHeight/2.5) - boxMargin
    
    # Draw caption
    
    font(fnames[2], 8)
    text("Weight: %s" % (100 * y + 100), (50, height()-50))
    
    # Box 1
    opticalsize = opMax
    textBox(textGenerator(opticalsize, 200), (margin, margin+bottomBoxHeight, boxWidth*2, topBoxHeight))
    text("OpSz: %s" % (opticalsize), (margin, margin+bottomBoxHeight+boxMargin*2-10))
    
    # Box 2
    opticalsize = opMax/3
    textBox(textGenerator(opticalsize, 200), (margin, margin, boxWidth-margin, bottomBoxHeight))
    text("OpSz: %s" % (opticalsize), (50,50))
    
    # Box 3
    opticalsize = opMin
    textBox(textGenerator(opticalsize, 500), ((boxMargin*2) + boxWidth, margin+boxMargin, boxWidth-margin, bottomBoxHeight))
    text("OpSz: %s" % (opticalsize), ((boxMargin*2) + boxWidth, margin))
    
## Uppercase Paragraph Settings, Roman Only

for y in range(0,pages,1):
    # textsamplenew = ""
    # for x in range(0,100,1):
    #     textsamplenew += choice(textsample) + " "
    newPage("TabloidLandscape")
    pageHeight = height()-(margin*2)
    boxMargin = (margin/2)
    boxWidth = (width()/2)- boxMargin
    topBoxHeight = pageHeight - boxMargin
    bottomBoxHeight = (pageHeight/2 - boxMargin)
    
    # Draw caption
    
    font(fnames[2], 8)
    text("Weight: %s" % (100 * y + 100), (50, height()-50))
    
    # Box 1
    opticalsize = opMax
    textBox(textGenerator(opticalsize, 200, fontpick = "Fraunces", isUpper=True), (margin, margin, boxWidth-boxMargin, topBoxHeight))
    text("OpSz: %s" % (opticalsize), (50, 50))
    
    # Box 2
    opticalsize = opMax/3
    textBox(textGenerator(opticalsize, 200, fontpick = "Fraunces", isUpper=True), ((boxMargin*2) + boxWidth, margin+bottomBoxHeight+boxMargin*2, boxWidth-margin, bottomBoxHeight))
    text("OpSz: %s" % (opticalsize), ((boxMargin*2) + boxWidth, margin+bottomBoxHeight+boxMargin*2-10))
    
    # Box 3
    opticalsize = opMin
    textBox(textGenerator(opticalsize, 500, fontpick = "Fraunces", isUpper=True), ((boxMargin*2) + boxWidth, margin+boxMargin, boxWidth-margin, bottomBoxHeight))
    text("OpSz: %s" % (opticalsize), ((boxMargin*2) + boxWidth, margin))
    
saveImage("PDFs/%s.pdf" % (newFileName))