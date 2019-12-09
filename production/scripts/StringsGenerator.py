f = CurrentFont()
g = CurrentGlyph()

# TODO: Translate color values to HEX string to avoid comparing floats
template = {
    #uppercase (red)
    (1.0, 0.0, 0.0, 1.0) : u"HH{}HH{}OO{}OO",
    #lowercase (yellow)
    (1.0, 1.0, 0.0, 1.0) : u"nn{}nn{}oo{}oo",
    #numerals (blue)
    (0.0, 0.0, 1.0, 1.0) : u"00{}00{}11{}11"
}

# Define results array
results = []

for name in f.keys():
    g = f[name]
    if g and g.unicode and g.mark and template[g.mark]:
        c = chr(g.unicode)
        # Append tuple of (color, glyph, template) to results
        results.append((g.mark, c , template[g.mark].format(c,c,c)))

# Results now contains an array of Tuples of the form
# [(color, glyph, template), ...]

# Sort the results using tuple comparison function
# which lexically sorts based off of ordinal position of
# items in tuple.
results.sort()

# Iterate through array of Tuples
# unpacking contents of Tuple into glyph and template, ignoring the color
for (_, glyph, template) in results:
    print(u"{}\t{}".format(glyph,template))