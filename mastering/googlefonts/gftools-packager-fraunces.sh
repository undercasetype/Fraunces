# !/bin/bash

# A script to use the gftools packager to push to the google/fonts GitHub repo
# See https://github.com/googlefonts/gftools/tree/master/docs/gftools-packager
#
# NOTE: You must have push access to google/fonts in order for this script to work

gftools packager mastering/googlefonts/upstream.yaml ~/type-repos/google-font-repos/fonts -f

# # If you wish to run FontBakery checks on the fonts in their natural habitat
# mkdir -p mastering/checks
# fontbakery check-googlefonts ~/type-repos/google-font-repos/fonts/ofl/fraunces/Fraunces\[SOFT,WONK,opsz,wght\].ttf --ghmarkdown mastering/checks/Fraunces.checks.md
# fontbakery check-googlefonts ~/type-repos/google-font-repos/fonts/ofl/fraunces/Fraunces-Italic\[SOFT,WONK,opsz,wght\].ttf --ghmarkdown mastering/checks/Fraunces-Italic.checks.md