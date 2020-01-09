#!/bin/sh
set -e

echo "Generating Static fonts"
mkdir -p ../fonts
mkdir -p ../fonts/static/otf
mkdir -p ../fonts/static/ttf


# generate static designspace referencing csv and variable designspace file
# later, this might not be done dynamically
# python ../mastering/scripts/generate_static_fonts_designspace.py

#fontmake -m current_masters/Roman/Fraunces_static.designspace -i -o ttf --output-dir ../fonts/static/ttf/
#fontmake -m current_masters/Roman/Fraunces_static.designspace -i -o otf --output-dir ../fonts/static/otf/
#fontmake -m current_masters/Italic/FrauncesItalic_static.designspace -i -o ttf --output-dir ../fonts/static/ttf/
#fontmake -m current_masters/Italic/FrauncesItalic_static.designspace -i -o otf --output-dir ../fonts/static/otf/

echo "Generating VFs"
fontmake -m current_masters/Roman/Fraunces.designspace -o variable --output-path ../fonts/Fraunces[GOOF,WONK,opsz,wght].ttf
#fontmake -m current_masters/Italic/FrauncesItalic.designspace -o variable --output-path ../fonts/Frances-Italic[GOOF,WONK,opsz,wght].ttf

rm -rf master_ufo/ instance_ufo/ instance_ufos/


# echo "Post processing"
# ttfs=$(ls ../fonts/static/ttf/*.ttf)
# for ttf in $ttfs
# do
# 	gftools fix-dsig -f $ttf;
# 	#ttfautohint $ttf "$ttf.fix";
# 	#mv "$ttf.fix" $ttf;
# done

vfs=$(ls ../fonts/*.ttf)
echo vfs
echo "Post processing VFs"
for vf in $vfs
do
	gftools fix-dsig -f $vf;
	#ttfautohint-vf --stem-width-mode nnn $vf "$vf.fix";
	#mv "$vf.fix" $vf;
done

echo "Fixing VF Meta"
# gftools fix-vf-meta $vfs;

echo "Dropping MVAR"
for vf in $vfs
do
	# mv "$vf.fix" $vf;
	ttx -f -x "MVAR" $vf; # Drop MVAR. Table has issue in DW
	rtrip=$(basename -s .ttf $vf)
	new_file=../fonts/$rtrip.ttx;
	rm $vf;
	ttx $new_file
	rm $new_file
done

echo "Fixing Hinting"
for vf in $vfs
do
	gftools fix-nonhinting $vf "$vf.fix";
	if [ -f "$vf.fix" ]; then mv "$vf.fix" $vf; fi
done

# for ttf in $ttfs
# do
# 	gftools fix-nonhinting $ttf "$ttf.fix";
# 	if [ -f "$ttf.fix" ]; then mv "$ttf.fix" $ttf; fi
# done

rm -f ../fonts/*.ttx
rm -f ../fonts/static/ttf/*.ttx
rm -f ../fonts/*gasp.ttf
rm -f ../fonts/static/ttf/*gasp.ttf

echo "Done"
