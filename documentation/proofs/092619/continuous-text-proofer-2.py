# Proof should look at masters and instances, with continuous text. Roman and Italic should be compared, but using some sort of markdown in the text file to indicate Italic text.

import datetime

## Variables

now = datetime.datetime.now()
newFileName = "continuous-text-proofer" + now.strftime("%Y_%m_%d-%H_%M_%S")

fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
frauncesVals = listFontVariations(fnames[0])
wghtMin = frauncesVals['wght']['minValue']
wghtMax = frauncesVals['wght']['maxValue']
opMin = frauncesVals['opsz']['minValue'] + 0.1
opMax = frauncesVals['opsz']['maxValue']

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10
pLength = 200

wikiText = "sampletext4.txt"
wikitext = open(wikiText, 'r', encoding="utf-8")
wikiText = wikitext.read()
wikitext.close()
#wikiText = wikiText.split(" ")

wikiText2 = "sampletext5.txt"
wikitext2 = open(wikiText2, 'r', encoding="utf-8")
wikiText2 = wikitext2.read()
wikitext2.close()
#wikiText2 = wikiText2.split(" ")

wikiText3 = "sampletext6.txt"
wikitext3 = open(wikiText3, 'r', encoding="utf-8")
wikiText3 = wikitext3.read()
wikitext3.close()
#wikiText3 = wikiText3.split(" ")

## Functions

# def paragrapher(opsize, fSize, weight, wank, texty):
#     wordCounter = len(texty)
#     text = FormattedString()   
#     text.fontVariations(opsz = opsize , wght = weight, WONK = wank )
#     italicCounter = 0
#     for word in texty:
#         if word == "<italic>":
#             italicCounter += 1
#             continue
#         if word == "</italic>":
#             italicCounter -= 1
#             continue
#         if italicCounter == 0 and wordCounter > 0:
#             text.append(word + " ", font = fnames[0], fontSize = fSize, fill = 0)
#         if italicCounter == 1 and wordCounter > 0:
#             text.append(word + " ", font = fnames[1], fontSize = fSize, fill = 0)
#         wordCounter -= 1
#     return text
        
# newPage("TabloidLandscape")
# textBox(paragrapher(18, 36, 0), (margin,margin*1.25, width()-(margin*2), height()-(margin*2.25)))
# font(fnames[2], 10)
# text("Weight: %s, Optical Size: %s, Wonk: %s" % (1,1,1), (50,50))

for x in (0, 400, 1000):
    for z in (9.1, 30, 144):
        for y in (0, 1):
            for f in (0,1):
                for textboy in (wikiText, wikiText2, wikiText3):
                    newPage("TabloidLandscape")
                    fontVariations(opsz = z, wght = x, WONK = y)
                    font(fnames[f], 24)
                    textBox(textboy, (margin,margin*1.25, width()-(margin*2), height()-(margin*2.25)))
                    font(fnames[2], 10)
                    text("Weight: %s, Optical Size: %s, Wonk: %s" % (x,z,y), (margin,margin))
            
#saveImage("PDFs/%s.pdf" % (newFileName))