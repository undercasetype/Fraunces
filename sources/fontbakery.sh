set +e

mkdir -p fontbakery

## Skip static checks, as they take too long. Use https://fonttools.github.io/fontspector/ instead.
# fontbakery check-googlefonts ./fonts/ttf/*.ttf --ghmarkdown fontbakery/ttf.md
# fontbakery check-googlefonts ./fonts/otf/*.otf --ghmarkdown fontbakery/otf.md
fontbakery check-googlefonts ./fonts/variable/*.ttf --ghmarkdown fontbakery/variable.md --full-lists
