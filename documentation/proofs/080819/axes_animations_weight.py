for x in range(100,1000,50):
    
    newPage(1000, 300)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)

    fontVariations(opsz = 48, wght = x)

    font("Fraunces", 102)

    text("Aggravators Here", (50,175))

    font("Fraunces Italic", 102)

    text("Aggravators Here", (50,60))
    
    font("Recur Mono", 10)
    
    text("Weight: %s" % (x), (10,10))
    
saveImage("test2.gif")