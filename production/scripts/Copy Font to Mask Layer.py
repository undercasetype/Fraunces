# coding: utf-8
# menuTitle : Copy Font to Mask Layer
# shortCut : command+shift+m

# Ethan Cohen 2019-11-10
# Selected font will be copied to a new layer in current font 
# along with a bounding box so you can compare spacing

import mojo

f = mojo.UI.SelectFont()

cf = CurrentFont()

for g in f:
    if g.name in cf:
        l = cf[g.name].getLayer(f.info.styleName.replace(" ", ""))
        l.clear()
        pen = l.getPointPen()
        g.drawPoints(pen)
        l.decompose()

        l.width = g.width
    
        pen = l.getPen()
        pen.moveTo((0, f.info.descender))
        pen.lineTo((0, f.info.ascender))
        pen.lineTo((g.width, f.info.ascender))
        pen.lineTo((g.width, f.info.descender))
        pen.closePath()