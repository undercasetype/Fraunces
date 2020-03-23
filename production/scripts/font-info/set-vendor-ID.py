fonts = AllFonts()

for font in fonts:
    font.info.openTypeOS2VendorID = "UCT"
    font.save()
    font.close()
    