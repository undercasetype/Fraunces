#!/bin/bash

# This script copies the latest builds to the google fonts dir in order to run QA checks and prep for a PR
#
# USAGE: 
# Install requirements with `pip install -U -r misc/googlefonts-qa/requirements.txt`
# 
# after  `sources/build.sh`
# call this script from the root of your inter repo, with the absolute path your your google/fonts repo
# `mastering/googlefonts/update-gfonts-repo.sh /Users/<username>/<path>/fonts`
#
# add `--push` to the end if you wish to push the result to GitHub

# -------------------------------------------------------------------
# UPDATE VARIABLES BELOW AS NEEDED

# name for this directory within google/fonts/ofl
gFontsSubDir="fraunces"

# paths; assumes the script is run from the base directory of fraunces
frauncesDir=$(pwd)
frauncesRomanVF=$frauncesDir/fonts/Fraunces\[SOFT,WONK,opsz,wght\].ttf
frauncesItalicVF=$frauncesDir/fonts/Fraunces-Italic\[SOFT,WONK,opsz,wght\].ttf

# for listing metadata
category="SERIF"
designer="Undercase Type, Phaedra Charles, Flavia Zimbardi"

# UPDATE VARIABLES ABOVE AS NEEDED
# -------------------------------------------------------------------

set -e
source venv/bin/activate

# Path to local google/fonts repo
gFontsDir=$1

# if argument is missing or is "--help"
if [[ -z "$gFontsDir" || "$gFontsDir" = "-h" || $gFontsDir = "--help" ]] ; then
    echo 'Add absolute path to your local Google Fonts Git directory, like:'
    echo 'sources/update-gfonts-repo.sh /Users/<username>/<path>/fonts'
    exit 2
fi

# option to push to GitHub. Without this, it will do a dry run.
pushToGitHub=$2

# -------------------------------------------------------------------
# get latest font version to use in PR commit message 
set +e

ttx -t head $frauncesRomanVF
fontVersion=v$(xml sel -t --match "//*/fontRevision" -v "@value" ${frauncesRomanVF/".ttf"/".ttx"})

echo $fontVersion

rm ${frauncesRomanVF/".ttf"/".ttx"}

set -e

# -------------------------------------------------------------------
# navigate to google/fonts repo, get latest, then clear branch & font subdirectory

cd $gFontsDir
git checkout master
git pull upstream master
git reset --hard
git checkout -B $gFontsSubDir
git clean -f -d
rm -r ofl/$gFontsSubDir

# -------------------------------------------------------------------
# copy fonts

mkdir -p ofl/$gFontsSubDir

cp $frauncesRomanVF    ofl/$gFontsSubDir/$(basename $frauncesRomanVF)
cp $frauncesItalicVF    ofl/$gFontsSubDir/$(basename $frauncesItalicVF)

# -------------------------------------------------------------------
# make or move basic metadata 

gftools add-font ofl/$gFontsSubDir # do this the first time, then edit as needed 

# update these to be accurate if needed
sed -i "" "s/SANS_SERIF/$category/g" ofl/$gFontsSubDir/METADATA.pb
sed -i "" "s/UNKNOWN/$designer/g" ofl/$gFontsSubDir/METADATA.pb

cp $frauncesDir/OFL.txt ofl/$gFontsSubDir/OFL.txt

cp $frauncesDir/DESCRIPTION.en_us.html ofl/$gFontsSubDir/DESCRIPTION.en_us.html

# -------------------------------------------------------------------
# copy static fonts

cp -r $frauncesDir/fonts/static ofl/$gFontsSubDir/static

# -------------------------------------------------------------------
# adds and commits new changes, then force pushes

if [[ $pushToGitHub = "--push" || $pushToGitHub = "--p" ]] ; then
    git add .
    git commit -m "$gFontsSubDir: $fontVersion added."

    # push to upstream branch (you must manually go to GitHub to make PR from there)
    # this is set to push to my upstream (google/fonts) rather than origin so that TravisCI can run
    git push --force upstream $gFontsSubDir
fi