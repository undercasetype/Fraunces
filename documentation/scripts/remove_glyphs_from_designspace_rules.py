from vanilla.dialogs import *
from mojo.UI import AskString
from fontTools.designspaceLib import DesignSpaceDocument

"""
Remove glyphs from designspace rules
2019_11_28 Benedikt Bramboeck, Alphabet

heavily based on https://github.com/arrowtype/varfont-prep/blob/master/remove-list-of-glyphs.py
"""

glyphsToDelete = AskString(
    'Input glyphnames to remove, then select designspace').replace("'", "").replace(",", "").split(" ")

instruction = f"select designspace to remove {glyphsToDelete} from"

docPath = getFile(
    instruction, allowsMultipleSelection=False, fileTypes=["designspace"])

doc = DesignSpaceDocument()
doc.read(*docPath)

for gName in glyphsToDelete:
    for rule in doc.rules:
        newSubs = []
        for sub in rule.subs:
            if gName not in sub:
                newSubs.append(sub)
        rule.subs = newSubs
doc.write(*docPath)
