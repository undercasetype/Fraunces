# RENDER WITH: http://www.drawbot.com/
# If run from the command line, this assumes you are in this script's directory

# from drawBot import *
import math

shortSample = "ADHESION adhesion"

pangrams = ["adhesion","ADHESION"]

maxopsz = 96.0
minopsz = 24.0
maxwght = 800.0
minwght = 100.0

for page in range(2):
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = maxopsz 
    
    pageMargin = 32

    def round_to_even(f):
        return math.floor(f / 2.) * 2

    lines = 5
    
    


    def placeText(fontName,margin, topMargin, line, varnum):
        # if fontName > "./LibreCaslonText-VF.ttf":
        #     fontVariations(wght=weight)
        
        font(fontName,fontSize)
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)
    
        if varnum >= 24:
            
            # fontVariations(opsz=varnum)
        
            font("VulfMono-Light", 8)
            captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
            textBox(str(floor(varnum)), captionBoxSize)
            
            if line == 0:
                
                # titleBox = (16, H-24, W-margin*2, boxHeight)
                
                left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
            
                textBox("opsz", (left, top, width, height))
                textBox("Fraunces Regular & Italic, " + str(fontSize) +"pt", (pageMargin*2, top, width, height ))
                
                dateWidth = 240
                textBox("January 24, 2019", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        interval = (maxopsz-minopsz)/(lines-1)
        opticalSize = round_to_even(maxopsz-(interval*line))
        print(opticalSize)
        fontSize = opticalSize
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = round_to_even(maxopsz - ((maxopsz-minopsz)/(lines+6))*line)
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin * line*2 + fontSize
        
        placeText("./fonts/Fraunces-VF.ttf",margin,topMargin, line, opticalSize)
        placeText("./fonts/FrauncesItalic-VF.ttf",margin,topMargin+boxHeight, line, opticalSize)


    # margin= fontSize
    margin= maxopsz
    boxHeight= fontSize
    lineHeight(fontSize*1)


    fill(0)
    font("VulfMono-Light", 8)
    # lineHeight(fontSize*1)

## Weight Change 72pt ##
    
for page in range(2):
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = 72 
    
    pageMargin = 32

    def round_to_even(f):
        return math.floor(f / 2.) * 2

    lines = 4
    
    


    def placeText(fontName,margin, topMargin, line, varnum):
        # if fontName > "./LibreCaslonText-VF.ttf":
        #     fontVariations(wght=weight)
        
        font(fontName,fontSize)
            
        # fontVariations(opsz=24)
        fontVariations(wght=varnum)
        
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)

        
        # fontVariations(opsz=24)
    
        font("VulfMono-Light", 8)
        captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
        textBox(str(floor(varnum)), captionBoxSize)
        
        if line == 0:
            
            # titleBox = (16, H-24, W-margin*2, boxHeight)
            
            left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
        
            textBox("wght", (left, top, width, height))
            textBox("Fraunces Regular & Italic, " + str(fontSize) +"pt", (pageMargin*2, top, width, height ))
            
            dateWidth = 240
            textBox("January 24, 2019", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        interval = (maxwght-minwght)/(lines-1)
        weightsize = minwght+(interval*line)
        print(weightsize)
        fontSize = 72
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = fontSize
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin * line*2 + fontSize
        
        placeText("./fonts/Fraunces-VF.ttf",margin,topMargin, line, weightsize)
        placeText("./fonts/FrauncesItalic-VF.ttf",margin,topMargin+boxHeight, line, weightsize)


    # margin= fontSize
    margin= maxopsz
    boxHeight= fontSize
    lineHeight(fontSize*1)


    fill(0)
    font("VulfMono-Light", 8)
    # lineHeight(fontSize*1)
    
## Weight Change 24pt ##

for page in range(2):
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = 72 
    
    pageMargin = 32

    def round_to_even(f):
        return math.floor(f / 2.) * 2

    lines = 10
    
    


    def placeText(fontName,margin, topMargin, line, varnum):
        # if fontName > "./LibreCaslonText-VF.ttf":
        #     fontVariations(wght=weight)
        
        font(fontName,fontSize)
            
        # fontVariations(opsz=24)
        fontVariations(wght=varnum)
        
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams[page-1], textBoxSize)

        
        # fontVariations(opsz=24)
    
        font("VulfMono-Light", 8)
        captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
        textBox(str(floor(varnum)), captionBoxSize)
        
        if line == 0:
            
            # titleBox = (16, H-24, W-margin*2, boxHeight)
            
            left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
        
            textBox("wght", (left, top, width, height))
            textBox("Fraunces Regular & Italic, " + str(fontSize) +"pt", (pageMargin*2, top, width, height ))
            
            dateWidth = 240
            textBox("January 24, 2019", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        interval = (maxwght-minwght)/(lines-1)
        weightsize = minwght+(interval*line)
        print(weightsize)
        fontSize = 24
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = fontSize
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin * line*2 + fontSize
        
        placeText("./fonts/Fraunces-VF.ttf",margin,topMargin, line, weightsize)
        placeText("./fonts/FrauncesItalic-VF.ttf",margin,topMargin+boxHeight, line, weightsize)


    # margin= fontSize
    margin= maxopsz
    boxHeight= fontSize
    lineHeight(fontSize*1)


    fill(0)
    font("VulfMono-Light", 8)
    # lineHeight(fontSize*1)
    
saveImage("./PDF/ChaunceyVariableProof001.pdf")
