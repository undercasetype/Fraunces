f = CurrentFont()

# for name in f.keys():
#     g = f[name]
#     # Removed "if g and" because it was pulling out fractions for some reason?
#     if g.unicode and g.mark and template[g.mark]:
#         c = chr(g.unicode)
#         # Append tuple of (color, glyph, template) to results
#         results.append((g.mark, c , template[g.mark].format(c,c,c)))
        
listguy = []

for glyph in f:
    if glyph.unicode is not None and glyph.mark is not None:
        listguy.append(chr(glyph.unicode))
        
listguy.sort()

for guy in listguy:
    print(guy*4)