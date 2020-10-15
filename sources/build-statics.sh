#!/bin/sh
set -e

# Only use this when necesdsary, are currently not all instances are defined in the VF designspace files.
# generate static designspace referencing csv and variable designspace file
# later, this might not be done dynamically
# python mastering/scripts/generate_static_fonts_designspace.py

## -------------------------------------------------------------
## Statics

echo "Generating Static fonts"

mkdir -p fonts/static/ttf
fontmake -m sources/Roman/Fraunces_static.designspace -i -o ttf --output-dir fonts/static/ttf/
fontmake -m sources/Italic/FrauncesItalic_static.designspace -i -o ttf --output-dir fonts/static/ttf/

# mkdir -p fonts/static/otf
# fontmake -m sources/Roman/Fraunces_static.designspace -i -o otf --output-dir fonts/static/otf/
# fontmake -m sources/Italic/FrauncesItalic_static.designspace -i -o otf --output-dir fonts/static/otf/


echo "Post processing"
ttfs=$(ls fonts/static/ttf/*.ttf)
for ttf in $ttfs
do
    gftools fix-dsig -f $ttf;
    if [ -f "$ttf.fix" ]; then mv "$ttf.fix" $ttf; fi
    # TODO? set up ttfautohint
    # ttfautohint $ttf "$ttf.fix";
    # if [ -f "$ttf.fix" ]; then mv "$ttf.fix" $ttf; fi
    # gftools fix-hinting $ttf;
    # if [ -f "$ttf.fix" ]; then mv "$ttf.fix" $ttf; fi
    gftools fix-nonhinting $ttf $ttf.fix
    mv  $ttf.fix $ttf                                    # TODO: add back hinting?
    python mastering/scripts/fixNameTable.py $ttf
done

rm -f fonts/static/ttf/*gasp.ttf 
