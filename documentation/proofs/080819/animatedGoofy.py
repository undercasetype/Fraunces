def drawText(goofyval, opSz, Wght, horiz, vert):
    font("Fraunces", 110)
    fontVariations(opsz = opSz, goof = goofyval, wght = Wght)
    text("hamburgers", (horiz, vert))
    font("Recur Mono", 18)
    text("Goofy: %s, OpSz: %s, Wght: %s" % (goofyval, opSz, Wght), (horiz, vert-80))

for x in range(1,100,5):
    newPage(800,800)
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)
    drawText(x,144,100,50*2,height()-200)
    drawText(x,144,500,50*2,height()-400)
    drawText(x,144,1000,50*2,height()-600)

saveImage("goofyChange.gif")