def easeInOutQuad(t):
    t *= 2
    if t < 1:
        return 0.5 * (t ** 2)
    else:
        t = 2 - t
        return 1 - 0.5 * (t ** 2)

for x in range(0,900,40):
    percent = easeInOutQuad(x/900)
    newPage(2000, 600)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)

    fontVariations(opsz = 48, wght = (percent*900)+100.1, GOOF = 100)
    font("Fraunces", 200)

    text("Fraunces Roman", (50*2,175*2))

    font("Fraunces Italic", 200)

    text("Fraunces Italic", (50*2,60*2))
    
    font("Recur Mono", 20)
    
    text("Weight: %s" % (int((percent*900)+100)), (10*2,10*2))
    
for x in range(900,0,-40):
    percent = easeInOutQuad(x/900)
    newPage(2000, 600)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)

    fontVariations(opsz = 48, wght = (percent*900)+100, GOOF = 100)
    font("Fraunces", 200)

    text("Fraunces Roman", (50*2,175*2))

    font("Fraunces Italic", 200)

    text("Fraunces Italic", (50*2,60*2))
    
    font("Recur Mono", 20)
    
    text("Weight: %s" % (int((percent*900)+100)), (10*2,10*2))
    
saveImage("weight_axis.gif")