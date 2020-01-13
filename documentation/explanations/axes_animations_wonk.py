def easeInOutQuad(t):
    t *= 2
    if t < 1:
        return 0.5 * (t ** 2)
    else:
        t = 2 - t
        return 1 - 0.5 * (t ** 2)

for x in range(0,900,100):
    percent = easeInOutQuad(x/900)
    newPage(2000, 600)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)
    if x <= 450:
        wonky = 0
    if x >= 450:
        wonky = 1
    fontVariations(opsz = 48, wght = 400, GOOF = 100, WONK = wonky)

    font("Fraunces", 200)

    text("Roman: hnms&", (50*2,175*2))

    font("Fraunces Italic", 200)

    text("Italic: bdhklvw&", (50*2,60*2))
    
    font("Recur Mono", 20)
    
    text("WONK: %s" % (wonky), (10*2,10*2))
    
for x in range(900,0,-100):
    percent = easeInOutQuad(x/900)
    newPage(2000, 600)
    
    fill(1,1,1)
    rect(0,0,width(),height())
    fill(0,0,0)
    if x <= 450:
        wonky = 0
    if x >= 450:
        wonky = 1
    fontVariations(opsz = 48, wght = 400, GOOF = 100, WONK = wonky)

    font("Fraunces", 200)

    text("Roman: hnms&", (50*2,175*2))

    font("Fraunces Italic", 200)

    text("Italic: bdhklvw&", (50*2,60*2))
    
    font("Recur Mono", 20)
    
    text("WONK: %s" % (wonky), (10*2,10*2))
    
saveImage("wonk_axis.gif")