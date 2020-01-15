import datetime

now = datetime.datetime.now()
newFileName = "character_comparisons" + now.strftime("%Y_%m_%d-%H_%M_%S")

path = "chars_to_chars.txt"
textstuff = open(path, "r", encoding="utf-8")
textread = textstuff.read()
textread = textread.split("\n")
textstuff.close()

fSize = 60

print(textread)
txt = FormattedString()

for line in textread:
    for x in (100, 400, 700, 900):
        txt.fontVariations(opsz = 9.1, wght = x)
        txt.append(line + "\n", font="Fraunces", fontSize = fSize, align = "center")
        txt.append(line + "\n", font="Fraunces Italic", fontSize = fSize, align = "center")

while len(txt) > 0:      
    newPage("LetterLandscape")
    font("Recur Mono", 10)
    text("Interpolation & Style Comparisons", (25,25))
    txt = textBox(txt, (50, 50, width()-100, height()-100))
    
txt = FormattedString()
    
for line in textread:
    txt.fontVariations(opsz = 9.1, wght = 400)
    txt.append(line + "\n", font="Fraunces", fontSize = fSize, align = "center")
    txt.append(line + "\n", font="Fraunces Beta Regular OpMin", fontSize = fSize, align = "center")
    txt.append(line + "\n", font="Fraunces Italic", fontSize = fSize, align = "center")
    txt.append(line + "\n", font="Fraunces Italic Beta Regular OpMin", fontSize = fSize, align = "center")
    txt.fontVariations(opsz = 9.1, wght = 700)
    txt.append(line + "\n", font="Fraunces", fontSize = fSize, align = "center")
    txt.append(line + "\n", font="Fraunces Beta Bold OpMin", fontSize = fSize, align = "center")
    txt.append(line + "\n", font="Fraunces Italic", fontSize = fSize, align = "center")
    txt.append(line + "\n", font="Fraunces Italic Beta Bold OpMin", fontSize = fSize, align = "center")
    
while len(txt) > 0:      
    newPage("LetterLandscape")
    font("Recur Mono", 10)
    text("Beta to Current Comparison", (25,25))
    txt = textBox(txt, (50, 50, width()-100, height()-100))
    
saveImage("PDFs/%s.pdf" % newFileName)