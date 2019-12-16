# coding: utf-8
# menuTitle : Replace glyphs marked yellow or red (or unmarked)

# Ethan Cohen 2019-11-27
# Replace glyphs that are marked red or yellow or have no mark with the version from the selected font.

import mojo

red = (1.0, 0.0, 0.0, 1.0)
yellow = (1.0, 1.0, 0.0, 1.0)
blue = (0.0, 0.0, 1.0, 0.5)

f = mojo.UI.SelectFont()
cf = CurrentFont()

for g in f:
    if g.name not in cf:
        cf.newGlyph(g.name)
    if cf[g.name].mark == yellow or cf[g.name].mark == red or cf[g.name].mark == None:
        l = cf[g.name].getLayer("foreground")
        l.clear()
        pen = l.getPointPen()
        g.drawPoints(pen)

        l.width = g.width    
    
        if g.unicode:
            cf[g.name].unicode = g.unicode
