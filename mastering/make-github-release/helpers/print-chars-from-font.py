
""" 
	Extended from https://stackoverflow.com/a/19438403
	
	USAGE:
	python checkfont.py /path/to/font.ttf

"""
#!/usr/bin/env python
from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

ttf = TTFont(sys.argv[1], 0, allowVID=0,
                ignoreDecompileErrors=True,
                fontNumber=-1)

chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)

for char in sorted(set(list(chars))):
	character = chr(char[0])
	print(character, end=" ")
	# if character in "\ ' \" \`":
	# 	print("\\" + character, end=" ")
	# else:
	# 	print(character, end=" ")

ttf.close()