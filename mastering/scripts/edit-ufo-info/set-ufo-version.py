'''
    Sets font version in UFOs

    USAGE:

    python <path>/mastering/scripts/edit-ufo-info/set-ufo-version.py sources/Italic 1.001 --save

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

# check for version number
save = False
try:
    if sys.argv[2]:
        print("Version to set is: ", sys.argv[2])
        newVersion = sys.argv[2].split(".")
except IndexError:
    print("Add a font version to set, like '1.001'")

# check whether to save new results
save = False
try:
    if sys.argv[3] == "-s" or sys.argv[3] == "--save" :
        print("Saving new version to fonts")
        save = True
except IndexError:
    print("Dry run. Add second arg of --save or -s to save new vertical metrics.")

# run program
for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    # font = defcon.Font(ufoPath)
    font = OpenFont(ufoPath, showInterface=False)

    print()
    print(font.info.familyName, font.info.styleName)
    print()
    print(f'version: {font.info.versionMajor} {font.info.versionMinor}')

    font.info.versionMajor = int(newVersion[0])
    font.info.versionMinor = int(newVersion[1])

    print()
    print(f'version now: {font.info.versionMajor} {font.info.versionMinor}')

    if save:
        font.update()
        font.save()
