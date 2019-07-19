import datetime

now = datetime.datetime.now()
newFileName = "xheight_overshoot_check" + now.strftime("%Y_%m_%d-%H_%M_%S")

fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
textsample = "oingo boingo "

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 7

for y in range(0,pages,1):
    newPage("LetterLandscape")
    pageHeight = height()-(margin*2)
    boxMargin = (margin/2)
    boxWidth = (width()/2)- boxMargin
    leftBoxHeight = pageHeight - boxMargin
    rightBoxHeight = (pageHeight/2 - boxMargin)
    for x in range()