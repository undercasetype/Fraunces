#!/bin/sh
set -e

# A script to generate woff2 files for variable & static fonts
# Required: woff2_compress (https://github.com/google/woff2)

## ------------------------------------------------------------------
## variable woff2

vfDir="fonts"
vfWebDir="fonts/web"

mkdir -p $vfWebDir

vfs=$(ls $vfDir/*.ttf)
echo vfs
echo "Making woff2 files from VFs"
for vf in $vfs
do
	woff2_compress $vf;

	woff2=$(basename -s .ttf $vf).woff2
	mv $vfDir/$woff2 $vfWebDir/$woff2
done

## ------------------------------------------------------------------
## static woff2

staticDir="fonts/static/ttf"
staticWebDir="fonts/web/static"

mkdir -p $staticWebDir

ttfs=$(ls $staticDir/*.ttf)
echo "Making woff2 files from static TTFs"
for ttf in $ttfs
do
	woff2_compress $ttf;

	woff2=$(basename -s .ttf $ttf).woff2
	mv $staticDir/$woff2 $staticWebDir/$woff2
done
