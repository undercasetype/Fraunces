# Fraunces Worklog - December 20th - Flavia

## Summary of current affairs

In the past couple of weeks I refined the structure files and generated all accented characters for the Roman masters. This Thursday/Friday, I was doing the same for the italics >> both Black masters are done. Spencer will finish the Light ones next week.

## The recipe for Glyph Construction

I am sure I could have coded the structure files and used anchors/guides in a smarter way, but the extension was a bit buggy evertime I tried to use different anchors for top & bottom alignments, so I decided to keep just one and call it "center", and then manually adjust whatever else that was needed in the code. That's why we have 2 structure files per master: one for the full char-set and other for alternates.

In the roman masters, top & bottom diacritics were infrequently in different positions, but this isn't true in the italics because of its slant, so more corrections are needed. 

* first copy all diacritics from its respective roman master and skew around 15 degrees (minus components).
* copy guides for vertical alignment.
* copy anchors for a good start on the horizontal alignment. Because the italics have more anchors I'd suggest to copy from its respective optical master. You can do it manually or write a script if you're feeling fancy :)
* open Glyph Construction and load a structure — from its respective roman master. immediately save as and renamed it.
* adjust anchors position in the base glyphs and diacritics if needed. 
* make edits in the code to fine tune alignments.    
* when everything is in place, generate glyphs. don't forget to save the structure again.
* duplicate this structure and rename to make the alternative shapes. leave only the necessary characters, delete the unicodes and add ".alt" to the end of each glyph name (final name & base glyph)
* load alts structure file, make the necessary edits, generate.
* load ligs (from the production folder), generate.

notes: 
1. The roman masters use a g.alt with a smaller ear for all accented characters. you will need to edit that in the italic structure files. 
2. d & l caron uses only the alt shape. so they are present in the full char-set structure, not the alts one.
3. ogonek characters need to be drawn/placed manually. Copy from roman. 



