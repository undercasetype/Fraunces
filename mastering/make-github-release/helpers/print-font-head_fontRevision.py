
""" 
	Extended from https://stackoverflow.com/a/19438403
	
	USAGE:
	python checkfont.py /path/to/font.ttf

"""

import sys
from fontTools.ttLib import TTFont

ttf = TTFont(sys.argv[1])

print("{:.3f}".format(ttf["head"].fontRevision))
