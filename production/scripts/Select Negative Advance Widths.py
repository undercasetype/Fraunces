# coding: utf-8
# menuTitle : Select Negative Advance Widths

# Ethan Cohen 2019-11-03

# Fraunces-LightOpMaxGoofyMax.ufo and Fraunces-BlackOpMaxGoofyMax.ufo
# were not test installing because a few glyphs (/hyphensoft /gnrl:hyphen
# /registered /fhook) had negative advance widths.

f = CurrentFont()

f.selection = list(g.name for g in f if g.width < 0)