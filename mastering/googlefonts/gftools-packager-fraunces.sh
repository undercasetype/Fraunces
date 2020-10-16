# !/bin/bash

# gftools packager \
#     mastering/googlefonts/upstream.yaml \
#     /Users/stephennixon/type-repos/google-font-repos/fonts \
#     -fpy

gftools packager mastering/googlefonts/upstream.yaml ~/type-repos/google-font-repos/fonts -p --no-source

# gftools qa -f ~/type-repos/google-font-repos/fonts/ofl/fraunces/*.ttf --fontbakery -o ./mastering/checks # not wor

# mkdir -p mastering/checks
# fontbakery check-googlefonts ~/type-repos/google-font-repos/fonts/ofl/fraunces/Fraunces\[SOFT,WONK,opsz,wght\].ttf --ghmarkdown mastering/checks/Fraunces.checks.md
# fontbakery check-googlefonts ~/type-repos/google-font-repos/fonts/ofl/fraunces/Fraunces-Italic\[SOFT,WONK,opsz,wght\].ttf --ghmarkdown mastering/checks/Fraunces-Italic.checks.md