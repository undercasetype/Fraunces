# RENDER WITH: http://www.drawbot.com/
# If run from the command line, this assumes you are in this script's directory

# from drawBot import *
import math

shortSample = "hamburgefontsiv"

pangrams = ["hamburgefontsiv"]

maxopsz = 72.0
minopsz = 9.1
maxwght = 1000.0
minwght = 100.0
regwght = 300.00
pagerange = range(1)

## Weight Change 72pt ##
    
for page in pagerange:
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = 60 
    
    pageMargin = 32
    
    lines = 10

    def round_to_even(f):
        return math.floor(f / 2.) * 2


    def placeText(fontName,margin, topMargin, line, varnum1, varnum2):
        if fontName == "./fonts/Fraunces-VF.ttf":
            fontVariations(wght=varnum1)
            fontVariations(opsz=varnum2)
        
        font(fontName,fontSize)
        
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)
    
        font("VulfMono-Light", 8)
        captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
        textBox(str(floor(varnum1)), captionBoxSize)
        
        if line == 0:
            
            # titleBox = (16, H-24, W-margin*2, boxHeight)
            
            left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
        
            textBox("OpSz Min • Fraunces", (left, top, width, height))
            
            dateWidth = 240
            textBox("January 24, 2019", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        interval = 100
        weightsize = minwght+(interval*line)
        print(weightsize)
        fontSize = 60
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = fontSize
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin * line + fontSize
        
        placeText("./fonts/Fraunces-VF.ttf",margin,topMargin, line, weightsize, minopsz)
        # placeText("./fonts/FrauncesItalic-VF.ttf",margin,topMargin+boxHeight, line, weightsize
        
## New Page

for page in pagerange:
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = 72 
    
    pageMargin = 32
    
    lines = 10

    def round_to_even(f):
        return math.floor(f / 2.) * 2


    def placeText(fontName,margin, topMargin, line, varnum1, varnum2):
        if fontName == "./fonts/Fraunces-VF.ttf":
            fontVariations(wght=varnum1)
            fontVariations(opsz=varnum2)
        
        font(fontName,fontSize)
        
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)

        
        # fontVariations(opsz=24)
    
        font("VulfMono-Light", 8)
        captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
        textBox(str(floor(varnum1)), captionBoxSize)
        
        if line == 0:
            
            # titleBox = (16, H-24, W-margin*2, boxHeight)
            
            left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
        
            textBox("OpSz Max • Fraunces", (left, top, width, height))
            
            dateWidth = 240
            textBox("January 24, 2019", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        interval = 100
        weightsize = minwght+(interval*line)
        print(weightsize)
        fontSize = 60
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = fontSize
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin * line + fontSize
        
        placeText("./fonts/Fraunces-VF.ttf",margin,topMargin, line, weightsize, maxopsz)
        # placeText("./fonts/FrauncesItalic-VF.ttf",margin,topMargin+boxHeight, line, weightsize
        
## New Page

for page in pagerange:
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = 72 
    
    pageMargin = 32
    
    lines = 10

    def round_to_even(f):
        return math.floor(f / 2.) * 2

    def placeTextStatic(fontName, margin, topMargin, line):
        font(fontName,fontSize)
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)
        captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
        textBox(str(floor(400)), captionBoxSize)

        if line == 0:
            left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight

    def placeText(fontName,margin, topMargin, line, varnum1, varnum2):
        if fontName == "./fonts/Fraunces-VF.ttf":
            fontVariations(wght=varnum1)
            fontVariations(opsz=varnum2)
        
        font(fontName,fontSize)
        
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)

        
        # fontVariations(opsz=24)
    
        font("VulfMono-Light", 8)
        captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
        textBox(str(floor(varnum1)), captionBoxSize)
        
        if line == 0:
            
            # titleBox = (16, H-24, W-margin*2, boxHeight)
            
            left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
        
            textBox("OpSz Max • Fraunces", (left, top, width, height))
            
            dateWidth = 240
            textBox("January 24, 2019", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        interval = 50
        weightsize = regwght+(interval*line)
        print(weightsize)
        fontSize = 60
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = fontSize
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin*2 * line + fontSize
        
        placeText("./fonts/Fraunces-VF.ttf",margin,topMargin, line, weightsize, minopsz)
        placeTextStatic("./fonts/Fraunces.ttf",margin,topMargin, line)

saveImage("./PDF/ChaunceyVariableProof001.pdf")
