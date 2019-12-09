## NOTE: Be careful! This script deletes glyphs from your font AND saves it! ##

fonts = AllFonts()
f = CurrentFont()
namelist = ["foursuperior", "kgreenlandic", "ipa:schwa"]

for font in fonts:
    for glyph in font:
        for name in namelist:
            if glyph.name == name:
                font.removeGlyph(glyph.name)
                print("Removed the %s glyph from %s" % (glyph.name, font.info.styleName))  
    font.save()