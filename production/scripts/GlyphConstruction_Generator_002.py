## TO DO:
    # Make list of exceptions for so that list only includes composite glyphs.
    # Exceptions: base glyphs, punctuation
    # Additional exception: replace i with dotlessi

# Reading of text files, and converts them into usable lists.

with open('glyphSorting/PLUS_composites_360.txt', 'r', encoding='latin1') as text2:
    # Composite Glyphs
    PlusComp = []
    for line in text2:
        linesplit = line.strip().rpartition(' ')
        PlusComp.append(linesplit[2])
    for i in PlusComp:
        i = i[:-2]
        
with open('glyphSorting/PLUS_composites_360.txt', 'r', encoding='latin1') as text2:
    # Composite Glyphs Name & Uni
    PlusCompDict = {}
    for line in text2:
        linesplit = line.strip().rpartition(' ')
        linesplitname = linesplit[2]
        PlusCompDict[linesplitname] = line[2:6]

with open('glyphSorting/PLUS_drawn_215.txt', 'r', encoding='latin1') as text2:
    # Drawn Glyphs (base)
    PlusDrawn = []
    for line in text2:
        linesplit = line.strip().rpartition(' ')
        PlusDrawn.append(linesplit[2])
            
with open('glyphSorting/PLUS_either_19.txt', 'r', encoding='latin1') as text3:
    # Either drawn or composite
    PlusEith = []
    for line in text3:
        linesplit = line.strip().rpartition(' ')
        PlusEith.append(linesplit[2])

# Looks at PlusDrawn list, and creates a dictionary that tags with "top" and "bottom" values

accent_dict = {}

for i in PlusDrawn[:118]:
    if ".case" in i:
        continue
    else:
        if "comb" in i:
            i = i[:-4]
            accent_dict[i] = "top"
for i in PlusDrawn[118:]:
    if ".case" in i:
        continue
    else:
        if "comb" in i:
            i = i[:-4]
            accent_dict[i] = "bottom"     
                
print(accent_dict)                

accentsDictstoGlyphCon = []
accentsDictstoGlyphCon_ignored = []

## OKAY, I have two lists. One with the name of accents, the other with the name of the the Glyphs that need to be constructed.

# Variables I need to define:
    # Accent vert position (depends on case and number of accents in glyph)
    # Upper or lower character
        # .case
        # {top_uc} or {top_lc}
        
# First, I'm going to generate a dictionary with all these variables. Then I'll refer to that dictionary to generate my text.

# This function returns variables depending on the case of the base glyph.
def caseVariables(baseglyph):
    if baseglyph.isupper():
        case = ".case"
        overvar = "{top_uc}"
    elif baseglyph.islower():
        case = ""
        overvar = "{top_lc}"
    
# This function returns a dictionary of the components in a glyph, and the ordered number of each component.    
def glyphDictGenerator(glyph, baseglyphs, accents):
    # returns dict of accents in glyph
    glyphdict = {}
    accentlist = ()
    for base in baseglyphs:
        if glyph[:2] == base and if glyph[:1] == base:
            baseglyph=glyph[:2]
        elif glyph[:1] == base:
            baseglyph=glyph[:1]
        if baseglyph = True:
            glyphdict = glyphdict + {baseglyph:0}
    for accent in accents:
        if accent in glyph:
            accentlist.append(accent)
    for accent in accentlist:
        for accent2 in accentlist:
            if accent in accent2 and accent != accent2:
                accentlist.pop(accent)
    
# AEacute
        