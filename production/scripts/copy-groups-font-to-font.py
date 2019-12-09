# Copy Groups from top layer font to other open fonts.

f = CurrentFont()

fonts = AllFonts()

for fontz in fonts:
    if fontz.groups !=  f.groups:
        fontz.groups.update(f.groups)
        print("Changed groups!")