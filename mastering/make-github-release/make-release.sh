# !/bin/bash
set -e

echo "----------------------------------------------------------------------------------"
echo "Getting font version of Roman variable font"
version=$(python mastering/make-github-release/helpers/print-font-head_fontRevision.py "fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")


echo "----------------------------------------------------------------------------------"
echo "Setting all fonts the same version number: $version"
allFonts=$(find fonts -type f -name "*.ttf"  -o -name "*.otf")
for font in $allFonts; do
    font-v write --ver=$version --sha1 "$font"
done


echo "----------------------------------------------------------------------------------"
echo "Making woff2 fonts"
sources/build-scripts/make-woff2s.sh


echo "----------------------------------------------------------------------------------"
echo "make vf subsets"
mastering/make-github-release/helpers/make-vf-subsets.sh


echo "----------------------------------------------------------------------------------"
echo "Copying fonts dir to version-numbered folder"
releaseDir="UnderCaseType_Fraunces_$version"
rm -rf $releaseDir
mkdir -p $releaseDir
cp -rf fonts/. $releaseDir


echo "----------------------------------------------------------------------------------"
echo "Sorting fonts"

mv $releaseDir/web "$releaseDir/Fonts - Web"

mkdir -p "$releaseDir/Fonts - Desktop/static"
mv $releaseDir/static "$releaseDir/Fonts - Desktop"

for vf in $(ls $releaseDir/*.ttf); do
    mv "$vf" "$releaseDir/Fonts - Desktop/$(basename $vf)"
done


echo "----------------------------------------------------------------------------------"
echo "Copying in release readme"
cp mastering/make-github-release/data/release-notes--all.md $releaseDir/README.md


echo "----------------------------------------------------------------------------------"
echo "Making zip for release"
if [ -f $releaseDir.zip ]; then rm $releaseDir.zip; fi
zip $releaseDir.zip -r $releaseDir -x .DS_*


echo ""
echo "Zip for release made at → $releaseDir.zip"
echo ""
echo "DONE!"
echo ""
