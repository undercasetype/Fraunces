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
        for g in (0, 50, 100):
            for op in (9.1, 72, 144):
                txt.fontVariations(opsz = op, wght = x, GOOF = g)
                txt.append(line + "\n", font="Fraunces", fontSize = fSize, align = "center")
                # txt.append(line + "\n", font="Fraunces Italic", fontSize = fSize, align = "center")

while len(txt) > 0:      
    newPage("LetterLandscape")
    font("Recur Mono", 10)
    text("Interpolation & Masters Comparisons", (25,25))
    txt = textBox(txt, (50, 50, width()-100, height()-100))
    