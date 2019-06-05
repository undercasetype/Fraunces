import math

pangrams = "hamburgefontsiv"

maxopsz = 72.0
minopsz = 9.1
maxwght = 1000.0
minwght = 100.0
regwght = 300.00

textSize = 60
pageMargin = 32
lines = 10
interval = 100
pagerange = range(1)

# def placeTextVariable(fontName, margin, topMargin, line, varnum1, varnum2):
#     font(fontName, fontSize)
#     fontVariations(wght=varnum1, opsz=varnum2)
#     textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
#     textBox(pangrams, textBoxSize)
    
def placeTextStatic(fontName, margin, topMargin, line):
    font(fontName, textSize)
    textBoxSize = (pageMargin*2, H-topMargin, W-pageMargin*3, boxHeight)
    textBox(pangrams, textBoxSize)
    
for page in pagerange:
    newPage('Letter')
    W,H = width(), height()
    font("./fonts/Fraunces.ttf", 60)
    text("Test", (200,600))
    
    for line in range(lines):
        margin = textSize
        boxHeight = textSize
        lineHeight(textSize*1)
        fill(0)
        fontSize(textSize)
        weightsize = minwght+(interval*line)
        topMargin = pageMargin*2 + margin * line + textSize
        # placeTextVariable("./fonts/Fraunces-VF.ttf", margin, topMargin, line, weightsize, minopsz)
        placeTextStatic("./fonts/Fraunces.ttf", margin, topMargin, line)
        