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
                
accentsDictstoGlyphCon = []
accentsDictstoGlyphCon_ignored = []

# Function that takes a list of Composite Glyphs, list of Base Glyphs, and an Accent Dictionary (which has values for the position of the accent), and formats them
# in a way that is recognizable for GlyphConstruction in Robofont.
def accentsDictsGenerator(compglyphs, baseglyphs, accentsdict):
    for glyph in compglyphs:
        glyphparsed = []
        for base in baseglyphs:
            if base[:1].isupper():
                case = ".case"
                position = 2
                overvar = "{top_uc}:"
            else:
                case = ""
                position = 0
                overvar = "{top_lc}:"
            #if glyph == accents or noncomb glyphs in PlusDrawn :
                # don't run anything below here and move on to the next base glyph
            if glyph[:2] == base:
                glyphparsed.append(glyph[:2])
                subglyph = glyph[2:]
                subglyphcounter = len(subglyph)
                subglyph2counter = 0
                while subglyph2counter <= subglyphcounter:
                    subglyph2 = subglyph[:subglyph2counter]
                    for accent in accentsdict.keys():
                        accentcounter = 0
                        if accent in subglyph2:
                            accentcounter += 1
                            glyphparsed.append("%s@%s,%s" % (accent+"%s" % (case), "center", overvar+accentsdict.get(accent)+"%s" % (str(position+accentcounter))))
                            subglyph = subglyph[len(accent):]
                        else:
                            continue
                    subglyph2counter += 1
            elif glyph[:1] == base:
                glyphparsed.append(glyph[:1])
                subglyph = glyph[1:]
                subglyphcounter = len(subglyph)
                subglyph2counter = 0
                while subglyph2counter <= subglyphcounter:
                    subglyph2 = subglyph[:subglyph2counter]
                    for accent in accentsdict.keys():
                        accentcounter = 0
                        if accent in subglyph2:
                            accentcounter += 1
                            glyphparsed.append("%s@%s,%s" % (accent+"%s" % (case), "center", overvar+accentsdict.get(accent)+"%s" % (str(position+accentcounter))))
                            subglyph = subglyph[len(accent):]
                        else:
                            continue
                    subglyph2counter += 1
            else:
                continue
        accentsDictstoGlyphCon.append("%s=%s+%s|%s" % (glyph, glyphparsed[0], "+".join(glyphparsed[1:]), compglyphs.get(glyph)))

# Plug in list of composites, list of bases, and accent dictionary here.               
accentsDictsGenerator(PlusCompDict, PlusDrawn, accent_dict)

# Sorts and prints the list that accentsDictsGenerator makes.
accentsDictstoGlyphCon.sort()
for i in accentsDictstoGlyphCon:
    print(i)
    
# for i in accentsDictstoGlyphCon:
#     nums = i.count("top3")
#     if nums >= 2:
#         newstring= i.replace("top3","butts",-1)
#         print(i.replace(i, newstring))
#     print(i)