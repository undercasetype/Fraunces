glyphlist = ["b", "d", "h", "l", "v", "w"]

for font in AllFonts():
    for glyph in font:
        for x in glyphlist:
            if glyph.name == x:
                glyphname = "%s.alt" % (x)
                print(glyphname)
                if glyphname not in font:
                    print("Not in font!")
                    font.newGlyph(glyphname)
                    print("Made a new glyph called %s" % (glyphname))
                    
for font in AllFonts():
    for glyph in font:
        for x in glyphlist:
            if glyph.name == "%s" % (x):
                print("Here is %s" % (glyph.name))
                for glyph2 in font:
                    if glyph2.name == "%s.alt" % (x):
                        print("here is %s" % (glyph2.name))
                        glyph2 = glyph.copy()
            