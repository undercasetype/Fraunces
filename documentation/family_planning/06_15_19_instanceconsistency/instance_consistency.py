for a in range(1,9,1):
    newPage("Letter")
    con = 1.68
    opticalsize = (80/9) * a
    fontSize = 9
    font("Recur Mono", fontSize)
    text("opsz: %s" % round((opticalsize)), (50, 50))
    for x in range(0,height()-100,int(height()/8)):
        fontSize = 72
        font("Fraunces", fontSize)
        hval = height()-x-100
        stroke(0,1,1)
        line((50,hval), (475,hval))
        line((50,hval+(fontSize*0.46)), (475,hval+(fontSize*0.46)))
        stroke(None)
        fontVariations(wght = x*con, opsz = opticalsize)

        text("bingo", (50,height()-x-100))

        font("Fraunces Italic", fontSize)
        fontVariations(wght = x*con, opsz = opticalsize)

        text("bingo", (275,height()-x-100))

        fontSize = 9
        font("Recur Mono", fontSize)
        text("weight: %s" % (x*con), (500, height()-x-100))

saveImage("instanceconsistency.pdf")
saveImage("instanceconsistency.gif")