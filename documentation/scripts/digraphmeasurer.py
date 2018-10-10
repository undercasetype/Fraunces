# Compare Widths of Digraphs

# Look at width of:
    #LJ NJ Lj Nj lj nj
    #L+J N+J L+j N+j l+j n+j
    #width of LJ = L+J, NJ = N+J, Lj = L+j, Nj = N+j, lj = l+j, nj = n+j
    
f = CurrentFont()

digraphs = ["LJ", "NJ", "Lj", "Nj", "lj", "nj"]

# function that measures the width of the digraph decomposed
def digraphmeasure(glyphname):
    digraphwidth = 0
    for character in glyphname:
        for glyph in f:
            if glyph.name == character:
                digraphwidth += glyph.width
    return(digraphwidth)


for glyph in f:
    for digraph in digraphs:
        if digraph == glyph.name:
            glyph.width = int(digraphmeasure(digraph))
            print("%s is now %s units wide." % (glyph.name, digraphmeasure(digraph)))
            