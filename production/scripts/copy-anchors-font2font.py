## Script to copy anchors from one font to another. ##

import mojo

f = mojo.UI.SelectFont()
cf = CurrentFont()

for g in f:
    if g.anchors:
        for anchor in g.anchors:
            aname = anchor.name
            acord = (anchor.x, anchor.y)
            cf[g.name].clearAnchors()
            cf[g.name].appendAnchor(aname, acord)