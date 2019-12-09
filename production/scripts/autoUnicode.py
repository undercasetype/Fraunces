font = CurrentFont()

for glyph in font:
    glyph.autoUnicodes()
    print(glyph.unicode)