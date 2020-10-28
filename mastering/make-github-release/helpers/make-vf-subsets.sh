# !/bin/bash

# A script to make subset woff2s for a given variable font file path
# USAGE: mastering/make-github-release/helpers/make-vf-subsets.sh "<FONTPATH>" "<FONTNAME>"

# -------------------------------------------------------------
# CONFIGURATION

fontPath="fonts/Fraunces[SOFT,WONK,opsz,wght].ttf"
fontName="Fraunces"
fontPathItalic="fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf"
fontNameItalic="Fraunces-Italic"
subsetDir="fonts/web/variable-subsets"
subsetReadme="mastering/make-github-release/data/subsets-readme.md"

# unicodes ranges pulled from the latin-basic unicode ranges for Roboto
latinBasicUni="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
# unicodes ranges pulled from the latin-vietnamese unicode ranges for Roboto
vietnameseUni="U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB"
# unicodes ranges pulled from the latin-ext unicode ranges for Roboto (which is more extensive than Fraunces)
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF"

# -------------------------------------------------------------
# ROMAN SUBSETS

echo "\nRoman"

mkdir -p $subsetDir/fonts

echo "→ Google Fonts Latin Basic subset"
latinBasicFile="$fontName--latin_basic.woff2"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinBasicFile --layout-features='*' --unicodes="$latinBasicUni"

echo "→ Google Fonts Latin Extended"
latinExtFile="$fontName--latin_ext.woff2"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFile --layout-features='*' --unicodes=$latinExtUni

echo "→ Google Fonts Vietnamese subset"
vietnameseFile="$fontName--vietnamese.woff2"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$vietnameseFile --layout-features='*' --unicodes=$vietnameseUni


# -------------------------------------------------------------
# ITALIC SUBSETS

echo "\nItalic"

mkdir -p $subsetDir/fonts

echo "→ Google Fonts Latin Basic subset"
latinBasicFileItalic="$fontNameItalic--latin_basic.woff2"
pyftsubset $fontPathItalic --flavor="woff2" --output-file=$subsetDir/fonts/$latinBasicFileItalic --layout-features='*' --unicodes="$latinBasicUni"

echo "→ Google Fonts Latin Extended"
latinExtFileItalic="$fontNameItalic--latin_ext.woff2"
pyftsubset $fontPathItalic --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFileItalic --layout-features='*' --unicodes=$latinExtUni

echo "→ Google Fonts Vietnamese subset"
vietnameseFileItalic="$fontNameItalic--vietnamese.woff2"
pyftsubset $fontPathItalic --flavor="woff2" --output-file=$subsetDir/fonts/$vietnameseFileItalic --layout-features='*' --unicodes=$vietnameseUni


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

/* ---------------------------------------------------------------------------- */
/* ITALICS */

/* Latin Basic, as defined by Google Fonts */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  font-weight: 100 900;
  font-style: italic;
  src: url('fonts/$latinBasicFileItalic') format('woff2');
  unicode-range: $latinBasicUni;
}

/* Latin extended, for diacritics in font which are not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  font-weight: 100 900;
  font-style: italic;
  src: url('fonts/$latinExtFileItalic') format('woff2');
  unicode-range: $latinExtUni;
}

/* Vietnamese glyphs not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  font-weight: 100 900;
  font-style: italic;
  src: url('fonts/$vietnameseFileItalic') format('woff2');
  unicode-range: $vietnameseUni;
}
"

# the string of characters is generated via sources/mastering/print-chars-from-font.py, then copied in

# chars=$(python3 mastering/make-github-release/helpers/print-chars-from-font.py "$fontPath")
charsLatin=$(python mastering/make-github-release/helpers/print-chars-from-uni_ranges-if_in_font.py "$fontPath" "$latinBasicUni")
charsViet=$(python mastering/make-github-release/helpers/print-chars-from-uni_ranges-if_in_font.py "$fontPath" "$vietnameseUni")
charsExt=$(python mastering/make-github-release/helpers/print-chars-from-uni_ranges-if_in_font.py "$fontPath" "$latinExtUni")

__HTML="\
<!DOCTYPE html>
<html lang='en'>
	<head>
		<meta charset='UTF-8'>
		<meta name='viewport' content='width=device-width, initial-scale=1.0'>
		<title>$fontName Subset</title>
		<link rel='stylesheet' href='fonts.css'>
		<style>
			html {
				font-family: $fontName, sans-serif;
				margin: 1rem;
			}
			body {
				max-width: 1400px;
				margin: 5rem auto 15rem;
			}
			h1 {
				font-size: 6rem;
			}
			h2, h3 {
				margin-top: 3em;
			}
			p {
				font-size: 48px;
				word-break: break-all;
				line-height: 1.75;
				letter-spacing: 0.3em;
				font-weight: 900;
				font-variation-settings: "SOFT" 100;
				text-align: justify;
			}
			.italic {
				font-style: italic;
			}
		</style>
	</head>
	<body>
		<h1>
			$fontName Subsets
		</h1>
		<h2>
			$fontName
		</h2>
		<h3>
			Latin Basic
		</h3>
		<p>
			$charsLatin
		</p>
		<h3>
			Latin Extended
		</h3>
		<p>
			$charsExt
		</p>
		<h3>
			Latin Vietnamese
		</h3>
		<p>
			$charsViet
		</p>
		<div class="italic">
			<h2>
				$fontNameItalic
			</h2>
			<h3>
				Latin Basic
			</h3>
			<p>
				$charsLatin
			</p>
			<h3>
				Latin Extended
			</h3>
			<p>
				$charsExt
			</p>
			<h3>
				Latin Vietnamese
			</h3>
			<p>
				$charsViet
			</p>
		</div>
	</body>
</html>
"

echo "$__CSS" > $subsetDir/fonts.css
echo "$__HTML" > $subsetDir/index.html
cp -f $subsetReadme $subsetDir/README.md

echo "\n"
echo Example webpage at → $(pwd)/$subsetDir/index.html
echo "\n"
