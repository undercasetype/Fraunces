
""" 
    Print string of characters in given unicode ranges.
	
	EXAMPLE USAGE:

	python print-chars-from-uni_ranges.py "/path/to/font.ttf" "U+0000-00FF,U+0131,U+0152-0153"

"""
#!/usr/bin/env python
from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import struct



ttf = TTFont(sys.argv[1], 0, allowVID=0,
                ignoreDecompileErrors=True,
                fontNumber=-1)

# get characters in font
charsChain = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)


charsInFont = " ".join([chr(num[0]) for num in list(charsChain)])

# split unicode ranges into a list
unicodeRanges=sys.argv[2].split(",")

chars = ""

# expand unicode ranges into a list
for item in unicodeRanges:

    uniRange = item.replace("U+","")

    if "-" in uniRange:
        # get integer for start & end of range
        start = int(f'0x{uniRange.split("-")[0]}', 16)
        end = int(f'0x{uniRange.split("-")[1]}', 16)

        # go through range
        for num in range(start, end+1):
            if chr(num) in charsInFont:
                # add to chars
                chars += chr(num) + " "
    else:
        # get integer
        num = int(f'0x{uniRange}', 16)
        if chr(num) in charsInFont:
            # add to chars
            chars += chr(num) + " "

print(chars)

