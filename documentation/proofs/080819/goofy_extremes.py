newPage(1600,1000)
fill(1,1,1)
rect(0,0,width(),height())
fill(0,0,0)

def drawText(goofyval, opSz, Wght, horiz, vert):
    font("Fraunces", 100)
    fontVariations(opsz = opSz, goof = goofyval, wght = Wght)
    text("hamburgers", (horiz, vert))
    font("Recur Mono", 18)
    text("Goofy: %s, OpSz: %s, Wght: %s" % (goofyval, opSz, Wght), (horiz, vert-80))

drawText(1,144,1000,50*2,height()-200)
drawText(100,144,1000,400*2,height()-200)
drawText(1,144,100,50*2,height()-400)
drawText(100,144,100,400*2,height()-400)
drawText(1,9.1,1000,50*2,height()-600)
drawText(100,9.1,1000,400*2,height()-600)
drawText(1,9.1,100,50*2,height()-800)
drawText(100,9.1,100,400*2,height()-800)

saveImage("goofyDeltas.png")