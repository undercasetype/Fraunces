import datetime

## Variables

now = datetime.datetime.now()
newFileName = "paragraph_proofs" + now.strftime("%Y_%m_%d-%H_%M_%S")

fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
frauncesVals = listFontVariations(fnames[0])
wghtMin = frauncesVals['wght']['minValue']
wghtMax = frauncesVals['wght']['maxValue']
opMin = frauncesVals['opsz']['minValue'] + 0.1
opMax = frauncesVals['opsz']['maxValue']
goofMin = frauncesVals['goof']['minValue']
goofMax = frauncesVals['goof']['maxValue']

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10
goofSteps = 3
pLength = 200
textHamburgerfontsiv = "sampletext.txt"

## Functions

# This function generates formatted strings by randomly picking from the two fonts (in this case Roman or Italic), using the size specified, and paragraph length specified.

def textGenerator(textPath, fSize, goofNum, pLength, pageNum, fontPick=None, track=None, whatCase=None):
    textstuff = open(textPath, "r", encoding="utf-8")
    textsample = textstuff.read()
    textstuff.close()
    if whatCase == "upper":
        textsample = textsample.upper()
    elif whatCase == "title":
        textsample = textsample.title()
    textsample = textsample.split(" ")
    text = FormattedString()
    for x in range(0, pLength, 1):    
        text.fontVariations(opsz = fSize , wght = (100*pageNum) + 100, goof = goofNum )
        if fontPick in fnames:
            text.append(choice(textsample) + " ", font = fnames[fnames.index(fontPick)], fontSize = fSize, fill = 0)
        elif fontPick == None:
            text.append(choice(textsample) + " ", font = choice(fnames[0:2]), fontSize = fSize, fill = 0)
    return text
    
# This function takes the FormattedStrings() and lays them out across pages.

def textDrawings(textPath, case = None, fontPicker = None):
    for g in (1,50,100):
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
            goofNumb = (g)
    
            # Draw caption
    
            font(fnames[2], 8)
            text("Weight: %s, Goofy: %s" % ((100 * y + 100), goofNumb), (50, height()-50))
    
            # Box 1
            opticalsize = opMax
            textBox(
                textGenerator(textPath, opticalsize, goofNumb,200, y, fontPick = fontPicker, whatCase = case), 
                (margin, margin+bottomBoxHeight, 
                boxWidth*2, topBoxHeight))
            text(
                "OpSz: %s" % (opticalsize), 
                (margin, margin+bottomBoxHeight+boxMargin*2-10))
    
            # Box 2
            opticalsize = opMax/3
            textBox(
                textGenerator(textPath, opticalsize, goofNumb, 200, y, fontPick = fontPicker, whatCase = case), 
                (margin, margin, boxWidth-margin, bottomBoxHeight))
            text(
                "OpSz: %s" % (opticalsize), 
                (50,50))
    
            # Box 3
            opticalsize = opMin
            textBox(
                textGenerator(textPath, opticalsize, goofNumb, 500, y, fontPick = fontPicker, whatCase = case), 
                ((boxMargin*2) + boxWidth, margin+boxMargin, boxWidth-margin, bottomBoxHeight))
            text("OpSz: %s" % (opticalsize), 
            ((boxMargin*2) + boxWidth, margin))

## Drawings

textDrawings(textHamburgerfontsiv, fontPicker = "Fraunces")
textDrawings(textHamburgerfontsiv, case = "upper", fontPicker = "Fraunces")
textDrawings(textHamburgerfontsiv, case = "title", fontPicker = "Fraunces")

saveImage("PDFs/%s.pdf" % (newFileName))