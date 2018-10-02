# GOAL: Create script that outputs Glyph Construction file based on specific list.
# METHOD: Using PLUS_Drawn as base, and PLUS_composites as final output, output list as text file in Glyph Construction language.
    ## capitals
    # "base_comb_glyph = base_glyph + comb_glyph.cap@hposition,vposition |univalue"
    ## lowercase
    # "base_comb_glyph = base_glyph + comb_glyph@hposition.vposition |univalue"

# Google Plus List:
    # Base Glyphs Sublist
        # Capitals Sublist
        # Lowercase Sublist
        # Smallcaps Sublist
    # Combining Accents Glyphs Sublist
        # Above Glyphs
        # Below Glyphs
    # Combined Glyphs Sublist (Final List?)
        
# FIRST: Identify comb_glyph in PLUS_Drawn, label vposition
# SECOND: Sort PLUS_composites list for capitals and lowercase.
# THIRD: Identify base_glyph in PLUS_Drawn, lable hposition
# FOURTH: Output list formatted in Glyph Construction Language

# Create lists from external text files
# Retain Unicode values for comb_glyphs

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

# Define dictionaries for accents
# Need to add horizontalval and unicodeval to dictionary values

accent_dict = {}

for i in PlusDrawn[:119]:
    if ".case" in i:
        continue
    else:
        if "comb" in i:
            i = i[:-4]
            accent_dict[i] = "top"
for i in PlusDrawn[120:]:
    if ".case" in i:
        continue
    else:
        if "comb" in i:
            i = i[:-4]
            accent_dict[i] = "bottom"     
                
accentsDictstoGlyphCon = []
accentsDictstoGlyphCon_ignored = []

def accentsDictsGenerator(glyphs, accents):
    for accent in accents.keys():
        for glyph in glyphs:
            # if the base glyph is in the combining glyph and some other conditions:
            if accent in glyph and len(accent) < len(glyph) and glyph not in str(accentsDictstoGlyphCon): # any of the lines in accentsDictstoGlyphCon:
                # format this string and add the base glyph
                accentsDictstoGlyphCon.append("%s = %s + %scomb@%s,%s | %s" % (glyph, glyph[:1], accent, "center", accents.get(accent), glyphs.get(glyph)))
            # if the the base glyph already exists as a line in accentsDictstoGlyphCon:
            if accent in glyph and any(line.startswith(glyph) for line in accentsDictstoGlyphCon):
                # find that line, insert formatted string before " |"
                line.replace(" |", "+ %scomb@%s,%s |" % (accent, "center", accents.get(accent))) #the string that begins with glyph
        # how do I sort the missing 62 glyphs to the accentsDictstoGlyphCon_ignored?

# I need a new function that parses the glyph, instead of comparing the accents to the glyph.
def accentsDictsGenerator2(glyphs, accents):
    for glyph in glyphs:
        glyphparsed = []
        exceptions = ["AE", "DZ", "OE", "ae", "DZ", "oe"]
        # define the base glyph
        for line in PlusDrawn:
            if glyph[:2] == line:
                glyphparsed.append(glyph[:2])
            elif glyph[:1] == line:
                glyphparsed.append(glyph[:1])
            # append that to the glyphparsed list
        # for every accent in the glyph
        ## accents need to be in order listed in glyph!
        for accent in accents.keys():
            if accent in glyph:
                glyphparsed.append("%scomb@%s,%s" % (accent, "center", accents.get(accent)))
        # using the glyphparsed list, compile and format a line that gets added to accentsDictstoGlyphCon
            #is +: the right way to concatenate?
        # print(glyphparsed)
        accentsDictstoGlyphCon.append("%s = %s + %s | %s" % (glyph, glyphparsed[0], " + ".join(glyphparsed[1:]), glyphs.get(glyph)))
        
# I need a new function that parses the glyph, instead of comparing the accents to the glyph.

# Something is broken in this function! But something is maybe kind of working.
def accentsDictsGenerator3(glyphs, accents):
    for glyph in glyphs:
        glyphparsed = []
        # look and see if first 2 letters of glyph match any base
        for base in PlusDrawn:
            if glyph[:2] == base:
                glyphparsed.append(glyph[:2])
                subglyph = glyph[2:]
# !! accent parsing isn't working here!!
                while subglyph == True:
                    counter = 0
                    subglyph = glyph[:counter]
                    for accent in accents.keys():
                        if accent in subglyph:
                            glyphparsed.append("%scomb@%s,%s" % (accent, "center", accents.get(accent)))
                            glyph = glyph[len(accent):]
                        else:
                            continue
                    counter += 1
            if glyph[:1] == base:
                glyphparsed.append(glyph[:1])
                subglyph = glyph[1:]
# !! accent parsing isn't working here!!
                while subglyph == True:
                    counter = 0
                    subglyph = glyph[:counter]
                    for accent in accents.keys():
                        if accent in subglyph:
                            glyphparsed.append("%scomb@%s,%s" % (accent, "center", accents.get(accent)))
                            glyph = glyph[len(accent):]
                        else:
                            continue
                    counter += 1
            else:
                continue
        accentsDictstoGlyphCon.append("%s = %s + %s | %s" % (glyph, glyphparsed[0], " + ".join(glyphparsed[1:]), glyphs.get(glyph)))


# Plug in list of composites and list of bases here                
accentsDictsGenerator3(PlusCompDict, accent_dict)

accentsDictstoGlyphCon.sort()

for i in accentsDictstoGlyphCon:
    print(i)

# print(len(accentsDictstoGlyphCon))
# print(len(accentsDictstoGlyphCon_ignored))
# print(len(PlusCompDict))