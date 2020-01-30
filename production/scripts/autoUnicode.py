for font in AllFonts():
    for glyph in font:
        glyph.autoUnicodes()
        print(glyph.unicode)