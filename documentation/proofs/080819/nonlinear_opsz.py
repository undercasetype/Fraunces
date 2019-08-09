steps = int((144-9)/30)

for x in range(144,9,-steps):
    newPage(500,500)
    fill(1,1,1)
    rect(0,0, width(),height())
    fill(0,0,0)
    font("Fraunces", 600)
    fontVariations(opsz = x, wght = 1000)
    text("n", (74,100))
    font("Recur Mono", 10)
    text("OpSz: %s" % (x), (50,50))
    
saveImage("linear.gif")