
""" 
    Find unicode values in font that are not in ranges given.

    E.g. useful if making a subset with pyftsubset for unicode ranges

	Extended from https://stackoverflow.com/a/19438403
	
	USAGE:
	python print-remaining-unicodes-in-font.py "/path/to/font.ttf" "unicode ranges"

"""
#!/usr/bin/env python
from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import struct


unicodesToRemove=sys.argv[2]

# open font file
ttf = TTFont(sys.argv[1], 0, allowVID=0,
                ignoreDecompileErrors=True,
                fontNumber=-1)

# get characters in font
chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)

unicodesInFont = [f'U+{("%04X" % char[0])}' for char in list(chars)]

# print(unicodesInFont)

# split unicodes to remove
ranges=unicodesToRemove.split(",")
# print(ranges)

unicodesToRemoveList = []

# expand unicode ranges into a list
for item in ranges:

    uniRange = item.replace("U+","")

    if "-" in uniRange:
        # get integer for start & end of range
        start = int(f'0x{uniRange.split("-")[0]}', 16)
        end = int(f'0x{uniRange.split("-")[1]}', 16)

        # go through range
        for num in range(start, end+1):
            # add to unicodesToRemoveList
            # unicodesToRemoveList.append(num)
            unicodesToRemoveList.append(f'U+{("%04X" % num)}')
    else:
        # get integer
        num = int(f'0x{uniRange}', 16)
        # add to unicodesToRemoveList
        # unicodesToRemoveList.append(num)
        unicodesToRemoveList.append(f'U+{("%04X" % num)}')

# print()
# print()
# print(unicodesToRemoveList)

remainingSubsetToMake = ",".join([u for u in unicodesInFont if u not in unicodesToRemoveList])

print(remainingSubsetToMake)

# for uniVal in unicodesInFont:
#     print(int(uniVal))