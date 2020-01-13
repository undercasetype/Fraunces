font = CurrentFont()

# for glyph in font:
#     for component in glyph.components:
#         if component.baseGlyph == "quotesingle":
#             print(glyph)
#             print("component here!")

for glyph in font:
    if glyph.selected == True:
        glyph.decompose()