#!/bin/sh
set -e

# A script to generate woff2 files for variable & static fonts
# Required: woff2_compress (https://github.com/google/woff2)

## ------------------------------------------------------------------
## variable woff2

vfs=$(ls fonts/*.ttf)
echo vfs
echo "Post processing VFs"
for vf in $vfs
do
	woff2_compress $vf;
done