# !/bin/bash

# Sets font version numbers for all OTF and TTF fonts in a given directory (and in its sub-directories)
# Requires font-v. See main repo README.md for instructions on venv setup.
# 
# USAGE:
# <path>/set-version-fonts-in-dir.sh <directory> <version>
# 
# mastering/make-github-release/helpers/set-version-fonts-in-dir.sh fonts 1.000
# 
# NOTE: You should remake woff2 files with `sources/build-scripts/make-woff2s.sh` 
# after you update version numbers, as font-v doesn’t currently change woff2 versions.

dir=$1
version=$2
versionFloat=$(awk '{print $1}' <<< "${version}")

echo $versionFloat

echo "----------------------------------------------------------------------------------"
echo "Setting all fonts the same version number: $version"
allFonts=$(find $dir -type f -name "*.ttf"  -o -name "*.otf")
for font in $allFonts; do
    font-v write --ver=$versionFloat --sha1 "$font"
done
