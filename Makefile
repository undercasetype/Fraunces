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
	sh sources/fontbakery.sh