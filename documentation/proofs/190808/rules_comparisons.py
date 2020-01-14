textHamburgerfontsiv = "sampletext.txt"
textstuff = open(textHamburgerfontsiv, 'r', encoding="utf-8")
textsample = textstuff.read()
textstuff.close()

newPage(1000*2,500*2)
fill(1,1,1)
rect(0,0,width(),height())
fill(0,0,0)

font("Fraunces", 48)
fontVariations(opsz = 48, goof = 50, wght = 400)
textBox(textsample, (50,75,width()/2-100,height()-125))
font("Recur Mono", 18)
text("OpSz > 48", (50,50))

font("Fraunces", 18)
fontVariations(opsz = 12, goof = 50, wght = 400)
textBox(textsample*10, (100+width()/2-100,75,width()/2-100,height()-125))
font("Recur Mono", 18)
text("OpSz < 18", (100+width()/2-100,50))

saveImage("rules_comparisons.png")