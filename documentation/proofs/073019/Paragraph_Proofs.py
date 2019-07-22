import datetime

now = datetime.datetime.now()
newFileName = "xheight_overshoot_check" + now.strftime("%Y_%m_%d-%H_%M_%S")

fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
textsample = "on no boingo gon on gin "

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10

#def textGenerator():
    # text = FormattedString()
    # for 
    # text.append("on no boingo gon gin ", font = fPick, fontSize = fSize, fill = 0)
    # return text
    
#def boxGenerator():

for y in range(0,pages,1):
    newPage("LetterLandscape")
    pageHeight = height()-(margin*2)
    boxMargin = (margin/2)
    boxWidth = (width()/2)- boxMargin
    leftBoxHeight = pageHeight - boxMargin
    rightBoxHeight = (pageHeight/2 - boxMargin)
    
    # Box 1
    fontVariations(wght = 100*y, opsz = 72)
    font(fnames[0], 72)
    
    textBox(textsample*100, (margin, margin, boxWidth-boxMargin, leftBoxHeight))
    
    # Box 2
    fontVariations(wght = 100*y, opsz = 54)
    font(fnames[0], 36)
    
    textBox(textsample*100, ((boxMargin*2) + boxWidth, margin+rightBoxHeight+boxMargin, boxWidth-margin, rightBoxHeight))
    
    # Box 3
    fontVariations(wght = 100*y, opsz = 24)
    font(fnames[0], 12)
    
    textBox(textsample*100, ((boxMargin*2) + boxWidth, margin, boxWidth-margin, rightBoxHeight))