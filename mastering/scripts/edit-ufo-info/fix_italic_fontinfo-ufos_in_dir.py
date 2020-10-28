'''
    Sets font info in UFOs to correct "Italic" style naming in fonts generated via FontMake from UFOs
        - Sets Italic fonts to have "Italic" in the Style Name rather than in the Family Name, as this effects the final font info

    Somewhat specific to the Fraunces project.

    USAGE:

    python <path>/mastering/scripts/set-font-info-ufos_in_dir.py sources/Italic --save

    (Without the --save option it will only do a dry run)
'''

import sys
import os
import subprocess
from fontParts.world import *
import defcon

# get font dir
try:
    if sys.argv[1]:
        print("Getting UFO paths")
        dirToUpdate = sys.argv[1]
        subDirs = next(os.walk(dirToUpdate))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

        head = dirToUpdate

except IndexError:
    print("Please include directory containing UFOs")

# check whether to save new results
save = False
try:
    if sys.argv[2] == "-s" or sys.argv[2] == "--save" :
        print("Saving new vertical metrics to fonts")
        save = True

except IndexError:
    print("Dry run. Add second arg of --save or -s to save new vertical metrics.")

# run program
for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    # font = defcon.Font(ufoPath)
    font = OpenFont(ufoPath, showInterface=False)


    print('--------------------------------------------------------')
    familyName = font.info.familyName
    print('familyName is:')
    print(familyName)

    styleName = font.info.styleName
    print('styleName is:')
    print(styleName)

    if "Italic" in familyName:
        font.info.familyName = familyName.replace(" Italic","")
        font.info.styleName = styleName + " Italic"
    
    print()
    print("now")
    print('familyName is:')
    print(font.info.familyName)

    print('styleName is:')
    print(font.info.styleName)
    print()
    print()


    if save:
        font.update()
        font.save()
