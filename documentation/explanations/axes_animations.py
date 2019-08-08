for x in range(0,10):
    print(x)

for x in range(9,144,5):
    
    newPage(1000, 300)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)

    fontVariations(opsz = x+0.1, wght = 1000)

    font("Fraunces", 102)

    text("The best bunions", (50,175))

    font("Fraunces Italic", 102)

    text("The best bunions", (50,60))
    
    font("Recur Mono", 10)
    
    text("Optical Size: %s" % (x), (10,10))
    
saveImage("test.gif")