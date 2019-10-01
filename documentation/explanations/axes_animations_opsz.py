def easeInOutQuad(t):
    t *= 2
    if t < 1:
        return 0.5 * (t ** 2)
    else:
        t = 2 - t
        return 1 - 0.5 * (t ** 2)

maxNum = 144-9
minNum = 9
frames = 30

steps = int((maxNum-minNum)/frames)

for x in range(maxNum,minNum,-steps):
    percent = easeInOutQuad(x/maxNum)
    newPage(2000, 600)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)

    fontVariations(opsz = (percent*maxNum)+9.1, wght = 400, GOOF = 0.1)

    font("Fraunces", 200)

    text("Fraunces Roman", (50*2,175*2))

    font("Fraunces Italic", 200)

    text("Fraunces Italic", (50*2,60*2))
    
    font("Recur Mono", 20)
    
    text("OpSz: %s" % (int((percent*maxNum)+9)), (10*2,10*2))
    
for x in range(minNum,maxNum,steps):
    percent = easeInOutQuad(x/maxNum)
    newPage(2000, 600)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)
    print(percent)
    fontVariations(opsz = (percent*maxNum)+9.1, wght = 400, GOOF = 0.1)

    font("Fraunces", 200)

    text("Fraunces Roman", (50*2,175*2))

    font("Fraunces Italic", 200)

    text("Fraunces Italic", (50*2,60*2))
    
    font("Recur Mono", 20)
    
    text("OpSz: %s" % (int((percent*maxNum)+9)), (10*2,10*2))
    
saveImage("opsz_axis.gif")