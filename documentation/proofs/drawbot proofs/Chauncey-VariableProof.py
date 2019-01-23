# RENDER WITH: http://www.drawbot.com/
# If run from the command line, this assumes you are in this script's directory

# from drawBot import *
import math

shortSample = "adhesion"

pangrams = "adhesion"

for page in range(6):
    newPage('Letter')
    # size('Letter')
    W, H = width(), height()
    
    # print(W, H)

   

    # fontSize = 16
    fontSize = 12 + page*4
    
    pageMargin = 32

    def round_to_even(f):
        return math.floor(f / 2.) * 2

    lines = int(floor(H / fontSize / 2.8))
    
    


    def placeText(fontName,margin, topMargin, line, optical=6):
        # if fontName > "./LibreCaslonText-VF.ttf":
        #     fontVariations(wght=weight)
        
        font(fontName,fontSize)
        textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
        textBox(pangrams, textBoxSize)
    
        if optical > 7:
            
            fontVariations(opsz=optical)
        
            font("VulfMono-Light", 8)
            captionBoxSize = (pageMargin, H-topMargin, W-margin*2, boxHeight)
            textBox(str(floor(optical)), captionBoxSize)
            
            if line == 0:
                
                # titleBox = (16, H-24, W-margin*2, boxHeight)
                
                left, top, width, height = pageMargin, H-pageMargin-fontSize/2, W-margin*2, boxHeight
            
                textBox("opsz", (left, top, width, height))
                textBox("Libre Caslon Text Roman & Italic, " + str(fontSize) +"pt", (pageMargin*2, top, width, height ))
                
                dateWidth = 240
                textBox("Nov 20, 2018", (W-dateWidth-left, top, dateWidth, height ), align="right")


    # fill(.95,.95,.95)
    # rect(0,0,W, H)


    for line in range(lines):
        
        opticalSize = round_to_even(6 + (72/lines)*line)
        
        lineHeight(fontSize*1)
        fill(0)
        
        margin = fontSize*1.2
        boxHeight = fontSize
        # topMargin = margin * line*2 + margin*3 - fontSize
        
        topMargin = pageMargin*2 + margin * line*2 + fontSize
        
        placeText("./fonts/ChauncyRegular-VF.ttf",margin,topMargin, line, optical=opticalSize)
        placeText("./fonts/ChauncyItalic-VF.ttf",margin,topMargin+boxHeight, line)


    # margin= fontSize
    margin= fontSize*1.2
    boxHeight= fontSize
    lineHeight(fontSize*1)


    fill(0)
    font("Vulf Mono", 8)
    # lineHeight(fontSize*1)
    
    # textBox("wght", (fontSize, H-fontSize*2, 100, 16))
    # textBox("Libre Caslon Text Roman & Italic, " + str(fontSize) +"pt", (margin*3,H-fontSize*2,400,16))

    # textBox("wght", (fontSize, H-32, 100, 16))
    # textBox("Libre Caslon Text Roman & Italic, " + str(fontSize) +"pt", (margin*3,H-32,400,16))


# imgPath = "../assets/weight-test-roman_italic-noblur-big-111918.mp4" # do 50 frames with a wght increase rate of 2 
imgPath = "../assets/weight-test-one_page-pangram-roman_italic-112018.pdf" # do 20 frames with a wght increase rate of 5
saveImage(imgPath)
# saveImage(imgPath, imageResolution=300)
