fonts = AllFonts()

f1 = fonts[0]
f2 = fonts[1]

for glyph in f1:
    if glyph.selected == True:
        print("Glyph selected!")
        for glyph2 in f2:
            if glyph2.name == glyph.name:
                glyph2 = glyph.copy()
                print("Copied %s glyph!" % (glyph.name))
                

        