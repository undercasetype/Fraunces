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

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10
pLength = 200
textHamburgerfontsiv = "sampletext.txt"
textstuff = open(textHamburgerfontsiv, 'r', encoding="utf-8")
textsample = textstuff.read()
textstuff.close()

## Functions

# This function generates formatted strings by randomly picking from the two fonts (in this case Roman or Italic), using the size specified, and paragraph length specified.

def textGenerator(textPath, fSize, pLength, pageNum, fontpick=None, track=None, whatCase=None):
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
        text.fontVariations(opsz = fSize , wght = (100*pageNum) + 100 )
        if fontpick in fnames:
            text.append(choice(textsample) + " ", font = fnames[fnames.index(fontpick)], fontSize = fSize, fill = 0)
        elif fontpick == None:
            text.append(choice(textsample) + " ", font = choice(fnames[0:2]), fontSize = fSize, fill = 0)
    return text
    
# This function takes the FormattedStrings() and lays them out across pages.

def textDrawings(textPath, case = None):

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
        textBox(
            textGenerator(textPath, opticalsize, 200, y, whatCase = case), 
            (margin, margin+bottomBoxHeight, 
            boxWidth*2, topBoxHeight))
        text(
            "OpSz: %s" % (opticalsize), 
            (margin, margin+bottomBoxHeight+boxMargin*2-10))
    
        # Box 2
        opticalsize = opMax/3
        textBox(
            textGenerator(textPath, opticalsize, 200, y, whatCase = case), 
            (margin, margin, boxWidth-margin, bottomBoxHeight))
        text(
            "OpSz: %s" % (opticalsize), 
            (50,50))
    
        # Box 3
        opticalsize = opMin
        textBox(
            textGenerator(textPath, opticalsize, 500, y, whatCase = case), 
            ((boxMargin*2) + boxWidth, margin+boxMargin, boxWidth-margin, bottomBoxHeight))
        text("OpSz: %s" % (opticalsize), e
        ((boxMargin*2) + boxWidth, margin))

## Drawings

for f in ("Fraunces", "Fraunces Italic"):
    for x in (9.1,144):
        for y in (100,1000):
            newPage("TabloidLandscape")
            font(f, 60)
            fontVariations(wght = y, opsz= x)
            textBox(textsample*100, (margin,margin, (width()-margin*2), (height()-margin*2)))
            font("Recur Mono", 9)
            text("OpSz: %s, Wght: %s" % (x,y), (50,50))
            
for f in ("Fraunces", "Fraunces Italic"):
    for x in (9.1,144):
        for y in (100,1000):
            newPage("TabloidLandscape")
            font(f, 60)
            fontVariations(wght = y, opsz= x)
            textBox(textsample.upper()*100, (margin,margin, (width()-margin*2), (height()-margin*2)))
            font("Recur Mono", 9)
            text("OpSz: %s, Wght: %s" % (x,y), (50,50))
            
def textGenerator2(textPath, opSz, pLength, weight, fontpick=None, track=None, whatCase=None):
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
        text.fontVariations(opsz = opSz, wght = weight)
        if fontpick in fnames:
            text.append(choice(textsample) + " ", font = fnames[fnames.index(fontpick)], fontSize = 60, fill = 0)
        elif fontpick == None:
            text.append(choice(textsample) + " ", font = choice(fnames[0:2]), fontSize = 60, fill = 0)
    return text
    
for x in (9.1,144):
    for y in (100,1000):
        newPage("TabloidLandscape")
        textBox(textGenerator2(textHamburgerfontsiv, x, 200, y), (margin,margin, (width()-margin*2), (height()-margin*2)))
        font("Recur Mono", 9)
        text("OpSz: %s, Wght: %s" % (x,y), (50,50))
        
for x in (9.1,144):
    for y in (100,1000):
        newPage("TabloidLandscape")
        textBox(textGenerator2(textHamburgerfontsiv, x, 200, y, whatCase = "upper"), (margin,margin, (width()-margin*2), (height()-margin*2)))
        font("Recur Mono", 9)
        text("OpSz: %s, Wght: %s" % (x,y), (50,50))
        
print(listFontVariations("Fraunces"))
            
saveImage("PDFs/%s.pdf" % (newFileName))