factor = 2
    
for font in AllFonts():
    for glyph in font:
        glyph.decompose()
    for glyph in font:
        glyph.scaleBy(factor)
        glyph.width *= factor
        for guide in glyph.guides:
            guide.x *= factor
            guide.y *= factor
    font.info.descender = int(round(font.info.descender * factor))
    font.info.xHeight   = int(round(font.info.xHeight   * factor))
    font.info.capHeight = int(round(font.info.capHeight * factor))
    font.info.ascender  = int(round(font.info.ascender  * factor))

    # Finally set new UPM
    font.info.unitsPerEm = font.info.unitsPerEm*factor
    font.update()
    font.save()