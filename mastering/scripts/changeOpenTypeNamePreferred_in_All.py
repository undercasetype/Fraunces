for f in AllFonts():
    f.info.openTypeNamePreferredFamilyName = "Fraunces"
    f.info.openTypeNamePreferredSubfamilyName = "Italic"
    f.save()
    f.close()