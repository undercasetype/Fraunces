# coding: utf-8
# menuTitle : Fraunces Test Install All
# shortCut : command+control+shift+t

# Ethan Cohen 2019-11-03

# Press command+control+shift+t to test install all open fonts.
# For any italic fonts, the script will move "italic" from the 
# family name to the style name, test install, then move "italic" 
# back to the family name, so you don't have to navigate to a 
# separate font family when proofing in adobe software.

for f in AllFonts():
    if "Italic" in f.info.familyName:
        f.info.familyName = f.info.familyName.replace(" Italic", "")
        f.info.styleName += " Italic"
        f.testInstall()
        f.info.familyName += " Italic"
        f.info.styleName = f.info.styleName.replace(" Italic", "")
    else:
        f.testInstall()