for font in AllFonts():
    print(font.info.familyName)
    font.info.familyName = "Fraunces Goofy"
    print(font.info.familyName)
    font.save()