# coding: utf-8
# menuTitle : Mark Glyphs re Components or Contours

# Ethan Cohen 2019-11-27
# If a glyph only has components it's marked yellow. Otherwise it's marked red.

f = CurrentFont()

red = (1.0, 0.0, 0.0, 1.0)
yellow = (1.0, 1.0, 0.0, 1.0)
blue = (0.0, 0.0, 1.0, 0.5)

for g in f:
    if g.components and not g.contours:
        g.mark = yellow
    else:
        g.mark = red