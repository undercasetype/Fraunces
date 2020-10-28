"""
    Checks for nested components in a TTF font.

    Thanks to Just van Rossum for this script snippet!
"""

from fontTools.ttLib import TTFont

p = 'fonts/Fraunces[SOFT,WONK,opsz,wght].ttf'

f = TTFont(p, fontNumber=0, lazy=True)

glyf = f["glyf"]

for gn in sorted(glyf.keys()):
    g = glyf[gn]
    if not g.isComposite():
        continue
    for c in g.components:
        if glyf[c.glyphName].isComposite():
            print(gn)

            c.decompose()

            break
