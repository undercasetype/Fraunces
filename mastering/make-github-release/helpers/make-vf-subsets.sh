# !/bin/bash

# A script to make subset woff2s for a given variable font file path
# USAGE: mastering/make-github-release/helpers/make-vf-subsets.sh "<FONTPATH>" "<FONTNAME>"


fontPath=$1
fontName=$2
subsetDir="$(dirname $fontPath)/variable-subsets"

echo $fontPath
echo $fontName
echo $subsetDir

mkdir -p $subsetDir/fonts

echo "→ Google Fonts Latin Basic subset"
latinBasicFile="$fontName--latin_basic.woff2"
latinBasicUni="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
# arrowsAndIcons="U+2190, U+2196, U+2191, U+2197, U+2192, U+2198, U+2193, U+2199, U+263a, U+2639, U+2661, U+2606, U+1f3b1, U+1f3b3, U+1f511, U+2702, U+1f45e, U+1f4f7, U+1f355, U+1f377, U+1f3b5, U+1f9fa"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinBasicFile --layout-features='*' --unicodes="$latinBasicUni"

echo "→ Google Fonts Vietnamese subset"
vietnameseFile="$fontName--vietnamese.woff2"
vietnameseUni="U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$vietnameseFile --layout-features='*' --unicodes=$vietnameseUni

echo "→ Google Fonts Latin Extended"
latinExtFile="$fontName--latin_ext.woff2"
# unicodes ranges pulled from the latin-ext unicode ranges for Roboto (which is more extensive than Fraunces)
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFile --layout-features='*' --unicodes=$latinExtUni


__CSS="\
/* Latin Basic, as defined by Google Fonts */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  font-weight: 100 900;
  src: url('fonts/$latinBasicFile') format('woff2');
  unicode-range: $latinBasicUni;
}

/* Latin extended, for diacritics in font which are not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  font-weight: 100 900;
  src: url('fonts/$latinExtFile') format('woff2');
  unicode-range: $latinExtUni;
}

/* Vietnamese glyphs not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  font-weight: 100 900;
  src: url('fonts/$vietnameseFile') format('woff2');
  unicode-range: $vietnameseUni;
}
"

# the string of characters is generated via sources/mastering/print-chars-from-font.py, then copied in

# chars=$(python3 mastering/make-github-release/helpers/print-chars-from-font.py "$fontPath")
chars=$(python mastering/make-github-release/helpers/print-chars-from-uni_ranges-if_in_font.py "$fontPath" "$latinBasicUni,$vietnameseUni,$latinExtUni")

__HTML="\
<!DOCTYPE html>
<html lang='en'>
	<head>
		<meta charset='UTF-8'>
		<meta name='viewport' content='width=device-width, initial-scale=1.0'>
		<title>$fontName Subset</title>
		<link rel='stylesheet' href='fonts.css'>
		<style>
			* {
				font-family: $fontName, sans-serif;
				font-weight: 900;
			}
			p {
				font-size: 48px;
				word-break: break-all;
				line-height: 1.75;
				letter-spacing: 0.3em;
			}
		</style>
	</head>
	<body>
		<h1>
			$fontName
		</h1>
		<p>
			$chars
		</p>
	</body>
</html>
"

echo "$__CSS" > $subsetDir/fonts.css
echo "$__HTML" > $subsetDir/index.html
# cp -f sources/mastering/data/subset-usage.md fonts/subsets/README.md
