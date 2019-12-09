f = CurrentFont()

# Write a script to update sidebearings of all group members based on group base glyph.

print(f.groups.findGlyph("O"))
    
for groupName in f.groups.keys(): 
    # maybe test this before
    
    # in this example the group name is "left_O"
    leftRight, keyGlyph = groupName.split("_")
    
    # check if the key glyph is in the font
    if keyGlyph not in f:
        continue
    keyGlyph = f[keyGlyph]
    
    # get all the glyphs from the group
    glyphs = f.groups[groupName]

    # loop over all the glyphs
    for destGlyph in glyphs:
        # check if the destination glyph is in the font
        if destGlyph not in f:
            continue
        # get the destination glyph 
        destGlyph = f[destGlyph]
        
        # based on the left or right copy the margins from the key glyph
        if leftRight == "left":
            destGlyph.leftMargin = keyGlyph.leftMargin
        
        elif leftRight == "right":
            destGlyph.rightMargin = keyGlyph.rightMargin