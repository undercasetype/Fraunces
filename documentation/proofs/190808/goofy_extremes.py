newPage(1600,1100)
fill(1,1,1)
rect(0,0,width(),height())
fill(0,0,0)

def drawText(goofyval, opSz, Wght, horiz, vert):
    font("Fraunces Italic", 100)
    fontVariations(opsz = opSz, goof = goofyval, wght = Wght)
    text("hamburgers", (horiz, vert))
    font("Recur Mono", 18)
    text("Goofy: %s, OpSz: %s, Wght: %s" % (goofyval, opSz, Wght), (horiz, vert-80))

drawText(1,144,1000,50*2,height()-300)
drawText(100,144,1000,400*2,height()-300)
drawText(1,144,100,50*2,height()-500)
drawText(100,144,100,400*2,height()-500)
drawText(1,9.1,1000,50*2,height()-700)
drawText(100,9.1,1000,400*2,height()-700)
drawText(1,9.1,100,50*2,height()-900)
drawText(100,9.1,100,400*2,height()-900)

text("Minimum Goofy", (50*2,height()-100))
text("Maximum Goofy", (400*2,height()-100))

saveImage("goofyDeltas_italic.png")