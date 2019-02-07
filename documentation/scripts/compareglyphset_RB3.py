from mojo.UI import SelectFont

markCounterpartsOfMissing = (1, 0, 0, 1)
# mark color for glyphs missing in the other font
# set to None for none, otherwise (r, g, b, a) tuple

f1 = SelectFont("Select 'Master' font:")
f2 = SelectFont("Select font to compare:")

if f1 is not None and f2 is not None:
    missing = []
    for glyph in f1:
        try:
            otherGlyph = f2[glyph.name]
        except:
            missing.append(glyph.name)
        
    print("%s misses the following glyphs compared to %s:" % (f2, f1))
    missing = sorted(missing)
    for m in missing:
        print(m)
        if markCounterpartsOfMissing is not None:
            f1[m].mark = markCounterpartsOfMissing
    
else:
    print("aborted")