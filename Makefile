# This file contains the main commands to build & check the fonts

# ---------------------------------------------------------------
# Configuration filepath

CONFIG=sources/build.yaml

# ---------------------------------------------------------------
# Commands

.PHONY: all
all: build checks

.PHONY: build
build:
	gftools builder $(CONFIG)
	pip freeze > requirements.freeze.txt

.PHONY: checks
checks:
	fontbakery check-googlefonts ./fonts/ttf/*.ttf --ghmarkdown > fontbakery/ttf.md
	fontbakery check-googlefonts ./fonts/otf/*.otf --ghmarkdown > fontbakery/otf.md
	fontbakery check-googlefonts ./fonts/variable/*.ttf --ghmarkdown > fontbakery/variable.md
