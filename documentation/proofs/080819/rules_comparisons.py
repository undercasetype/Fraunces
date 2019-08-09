textHamburgerfontsiv = "sampletext.txt"
textstuff = open(textHamburgerfontsiv, 'r', encoding="utf-8")
textsample = textstuff.read()
textstuff.close()

newPage(1000,500)
fill(1,1,1)
rect(0,0,width(),height())
fill(0,0,0)

font("Fraunces", 18)
fontVariations(opsz = 13, goof = 50, wght = 400)
textBox(textsample, (50,75,width()/2-100,height()-125))
font("Recur Mono", 10)
text("OpSz > 18", (50,50))

font("Fraunces", 18)
fontVariations(opsz = 12, goof = 50, wght = 400)
textBox(textsample, (100+width()/2-100,75,width()/2-100,height()-125))
font("Recur Mono", 10)
text("OpSz < 18", (100+width()/2-100,50))

saveImage("rules_comparisons.png")