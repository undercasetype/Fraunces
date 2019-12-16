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

if "GoofyMax" in s:
    l = g.getLayer(s.replace(" ", "").replace("GoofyMax", "GoofyMin"))
else:
    l = g.getLayer(s.replace(" ", "").replace("GoofyMin", "GoofyMax"))

g.width = l.width