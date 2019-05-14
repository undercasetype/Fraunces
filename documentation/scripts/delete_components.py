f = CurrentFont()

for glyph in f:
    for component in glyph.components:
        print(component.glyph)