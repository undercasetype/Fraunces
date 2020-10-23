'''
    Sets UFO styleName to excluded name "Sharp", as this effects the final font info in fonts generated via FontMake from UFOs.

    Somewhat specific to the Fraunces project.

    USAGE:

    python <path>/mastering/scripts/elide_sharp_name_fontinfo-ufos_in_dir.py sources/Roman --save
    python <path>/mastering/scripts/elide_sharp_name_fontinfo-ufos_in_dir.py sources/Italic --save

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
        print("Adjusting font info in UFOs...")
        save = True

except IndexError:
    print("Dry run. Add second arg of --save or -s to save adjusted font info.")

# run program
for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    # font = defcon.Font(ufoPath)
    font = OpenFont(ufoPath, showInterface=False)
    
    styleName = font.info.styleName

    if "Sharp" in styleName:

        print('--------------------------------------------------------')
        familyName = font.info.familyName
        print('familyName is:')
        print(familyName)

        styleName = font.info.styleName
        print('styleName is:')
        print(styleName)

        font.info.styleName = styleName.replace(" Sharp","")
    
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
    else:
        print("Dry run. Add second arg of --save or -s to save adjusted font info.")
