from ufoLib2 import Font
import argparse
from pathlib import Path

# set up argument parser
parser = argparse.ArgumentParser(description="Format UFO files in a directory.")
parser.add_argument("fontpaths", type=Path, nargs='+', help="Paths pointing to UFO files")
args = parser.parse_args()

fontpaths = args.fontpaths

for fontpath in fontpaths:
    font = Font.open(fontpath)
    font.save(fontpath, overwrite=True)
    print(f"Formatted {fontpath}")
