#!/bin/sh
set -e

## ------------------------------------------------------------------
## Variable Fonts Build - Static build is at sources/build-statics.sh

echo "Generating VFs"
mkdir -p fonts
fontmake -m sources/Roman/Fraunces.designspace -o variable --output-path fonts/Fraunces[SOFT,WONK,opsz,wght].ttf
fontmake -m sources/Italic/FrauncesItalic.designspace -o variable --output-path fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf

vfs=$(ls fonts/*.ttf)
echo vfs
echo "Post processing VFs"
for vf in $vfs
do
	gftools fix-dsig -f $vf;
	#python mastering/scripts/fix_naming.py $vf;
	#ttfautohint-vf --stem-width-mode nnn $vf "$vf.fix";
	#mv "$vf.fix" $vf;
done

echo "Fixing Hinting"
for vf in $vfs
do
	gftools fix-nonhinting $vf "$vf.fix";
	if [ -f "$vf.fix" ]; then mv "$vf.fix" $vf; fi
done

echo "Add STAT table"
python mastering/scripts/add_STAT-improved.py "fonts/Fraunces[SOFT,WONK,opsz,wght].ttf"
python mastering/scripts/add_STAT-improved.py "fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf"

rm -rf fonts/*gasp*

echo "Remove unwanted fvar instances"
for vf in $vfs
do
	python mastering/scripts/removeUnwantedVFInstances.py $vf
done

echo "Dropping MVAR"
for vf in $vfs
do
	# mv "$vf.fix" $vf;
	ttx -f -x "MVAR" $vf; # Drop MVAR. Table has issue in DW
	rtrip=$(basename -s .ttf $vf)
	new_file=fonts/$rtrip.ttx;
	rm $vf;
	ttx $new_file
	rm $new_file
done

echo "Fix name table"
for vf in $vfs
do
    python mastering/scripts/fixNameTable.py $vf
done


### Cleanup


rm -rf ./*/instances/

rm -f fonts/*.ttx
rm -f fonts/static/ttf/*.ttx
rm -f fonts/*gasp.ttf
rm -f fonts/static/ttf/*gasp.ttf

echo "Done Generating"

# echo "Checking VFs with FontBakery"
# mkdir -p mastering/checks
# fontbakery check-googlefonts fonts/Fraunces\[SOFT,WONK,opsz,wght\].ttf --ghmarkdown mastering/checks/Fraunces.checks.md
# fontbakery check-googlefonts fonts/Fraunces-Italic\[SOFT,WONK,opsz,wght\].ttf --ghmarkdown mastering/checks/Fraunces-Italic.checks.md
