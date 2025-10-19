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
	rm -rf sources/Roman/instance_ufos
	rm -rf sources/Italic/instance_ufos
	gftools builder $(CONFIG)
	pip freeze > requirements.freeze.txt

.PHONY: checks
checks:
	sh sources/fontbakery.sh