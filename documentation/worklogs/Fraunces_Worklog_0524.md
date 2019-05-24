# Fraunces Worklog: May 24th

_Flavia_
Today, I finished compiling the extended Character Set *see documentation/Fraunces GooglePlus CharSet*. I took out all the extra glyphs like IJ/ IJacute because it would make more sense to build up the language support later, with more research on what else might be missing from Google's list. And also addressed diacritics names/unicode values.

The latest *Fraunces_OpticalMax* source reflects that new CharSet and organization, and have most glyphs done with exception of what's marked in red and accenteded characters that need to be placed correctly.

In an effort to color code things and make searching for certain groups easier, all glyphs that are just components are marked with light purple (214, 222, 255). Alternates, orange (253, 196, 79); Glyphs that still need to be drawn, red (253, 93, 83); Ligatures, light green (217, 251, 147); Diacritics for typing, dark purple (194, 164, 213); Combining Diacritics, yellow (255, 250, 85), Diacritics altered to work together, light blue (126, 211, 253); Cap forms, pink (254, 160, 215), Accents that are on the list but haven't been used, dark blue (84, 161, 252) — we can change this later and even add more colors to cover parts of the process like, if it's 100% done or needs to be proofed, etc.

I then re-wrote the structure file for Glyph Builder *see documentation/scripts/GooglePlus_003_fz.glyphConstruction*: following the new accents names and logic for combining diacritics. Vietnamese comb accents like, circunflexacute should be one glyph in order to allow us to shape it in a better way. Cap forms are slighted compressed vertically to use less space. Bottom accents are the same across the board. Ohorn & Uhorn are a base glyph and not made of components anymore, as well as all ogonek comb glyphs. 

When expanding the new masters to this CharSet, new global guides (for vertical metrics) and anchors (for horizontal placement) will be needed — but the vertical metrics should be the same for all masters within one axis. Right now, all accents are vertically aligned within each other and placed vertically on the spot that works for lowercase. All cap forms should shift up together).