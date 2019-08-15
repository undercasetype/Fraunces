steps = int((144-9)/30)

for x in range(144,9,-steps):
    newPage(300,300)
    fill(1,1,1)
    rect(0,0, width(),height())
    fill(0,0,0)
    font("Fraunces", 300)
    fontVariations(opsz = x, goof = 1, wght = 1000)
    text("n", (40,50))
    font("Recur Mono", 10)
    text("Non-Linear Interpolation, OpSz: %s" % (x), (25,25))
    
saveImage("nonlinear.gif")