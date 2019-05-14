f = CurrentFont()

for glyph in f:
    if ".case" in glyph.name:
        newglyphname = glyph.name[:-9]+".case"
        glyph.name = newglyphname