# coding: utf-8
# menuTitle : Steal Glyph Width from Goof Counterpart
# shortCut : command+shift+2

# Ethan Cohen 2019-12-07

# If you are working on GoofyMin, steal the glyph width
# from the GoofyMax layer. If you are working on GoofyMax,
# steal the glyph width from GoofyMin layer.

f = CurrentFont()
g = CurrentGlyph()

s = f.info.styleName

if "G100" in s:
    l = g.getLayer(s.replace(" ", "").replace("G100", "G0"))
else:
    l = g.getLayer(s.replace(" ", "").replace("G0", "G100"))

g.width = l.width