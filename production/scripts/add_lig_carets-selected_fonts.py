"""
    Add `caret` anchors to ligature glyphs with approximate placement.

    USAGE:

    Run in RoboFont, then select UFOs to automatically add ligature carets to. 

    Positioning should be manually fixed afterwards (if the ligatures aren’t just composed from the base glyphs).
"""

from vanilla.dialogs import *

# name ligatures to look for
ligatures = [
    "f_f_i",
    "f_f_l",
    "f_f",
    "fi",
    "fl",
    "fl.alt",
    "f_f_l.alt",
    "lj.alt",
    "lj",
    "nj",
]

# get files
files = getFile("Select files to modify", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    font = OpenFont(file, showInterface=True)

    print("\n\n--------------------------------------------------\n")
    print(font.info.styleName)

    for glyphName in font.keys():
        if glyphName in ligatures:

            print()
            print(glyphName)
            # .appendAnchor("top", (10, 20))

            g = font[glyphName]

            simpleName = glyphName.replace("_","").replace(".alt","")

            widthCounter = 0
            for index, char in enumerate(simpleName):
                # do this one less time than the full length
                if index != len(simpleName) - 1 and f"caret_{index+1}" not in [a.name for a in g.anchors]:
                    # g.appendAnchor(f"caret_{index+1}", (g.width/len(simpleName)*(index+1),0))
                    # print(f"add anchor 'caret_{index+1}' at x={g.width/len(simpleName)*(index+1)}" )

                    widthCounter += font[char].width
                    g.appendAnchor(f"caret_{index+1}", (widthCounter,0))
                    print(f"added anchor 'caret_{index+1}' at x={widthCounter}" )
