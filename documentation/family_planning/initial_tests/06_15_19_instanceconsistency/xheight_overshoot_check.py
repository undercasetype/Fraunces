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
    boxHeight = (pageHeight/steps) - boxMargin
    boxWidth = width()-100
    for x in range(0,steps,1):
        fsize = 32
        osize = (72/pages)*y+7
        weight = (((1000+(1000/steps))/steps)*x)
        font("Recur Mono", 9)
        text("%s" % (round(weight)), (50, margin+(margin*(x/2))+(boxHeight*x)+boxMargin-10))
        txt = FormattedString()
        txt.fontVariations(opsz=osize, wght=weight)
        txt.append(textsample, font = "Fraunces", fontSize = fsize , fill = (0))
        txt.append(textsample, font = "Fraunces Italic", fontSize = fsize , fill = (0))
        txt.append(textsample, font = "Fraunces", fontSize = fsize , fill = (0))
        textBox(txt, (50, margin+(margin*(x/2))+(boxHeight*x)+boxMargin, boxWidth, boxHeight))
        print(osize)
        print(weight)
        
saveImage("%s.pdf" % (newFileName))
#saveImage("%s.gif" % (newFileName))