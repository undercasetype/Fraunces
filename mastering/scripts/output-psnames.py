import os
from fontTools.ttLib import TTFont
import sys

"""
    Use FontTools TTlib to output a list of PostScript Names (NameID 6) from all fonts in a directory.
"""

def get_postscript_name(font_path):
    try:
        font = TTFont(font_path)
        name = font['name'].getName(6, 3, 1) or font['name'].getName(6, 1, 0)
        if name:
            return name.toUnicode()
    except Exception as e:
        print(f"Error reading {font_path}: {e}")
    return None

def list_fonts_psnames(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.ttf', '.otf', '.ttc', '.otc')):
            font_path = os.path.join(directory, filename)
            ps_name = get_postscript_name(font_path)
            if ps_name:
                print(f"{filename}: {ps_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python output-psnames.py <directory>")
    else:
        list_fonts_psnames(sys.argv[1])