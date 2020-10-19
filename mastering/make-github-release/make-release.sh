


subsetDir="$outputDir/subsets/$fontName"

mkdir -p $subsetDir/fonts

## Google Fonts Latin Basic subset
latinBasicFile="$fontName--latin_basic.woff2"
latinBasicUni="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
arrowsAndIcons="U+2190, U+2196, U+2191, U+2197, U+2192, U+2198, U+2193, U+2199, U+263a, U+2639, U+2661, U+2606, U+1f3b1, U+1f3b3, U+1f511, U+2702, U+1f45e, U+1f4f7, U+1f355, U+1f377, U+1f3b5, U+1f9fa"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinBasicFile --layout-features='*' --unicodes="$latinBasicUni,$arrowsAndIcons"

## Google Fonts Latin Ext subset
latinExtFile="$fontName--latin_ext.woff2"
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF,U+2116,U+2122,U+2190,U+2192,U+2196,U+2197,U+2198,U+2199,U+2219,U+2248,U+2260,U+2264,U+2265,U+27e8,U+27e9"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFile --layout-features='*' --unicodes=$latinExtUni
# pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFile --layout-features='*' --unicodes-file="sources/mastering/data/latin-ext_unique-glyphs.nam" ### problem: how do we get the appropriate unicode values for the CSS?

# sources/mastering/data/latin-ext_unique-glyphs.nam

## Google Fonts Vietnamese subset
vietnameseFile="$fontName--vietnamese.woff2"
vietnameseUni="U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB"
pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$vietnameseFile --layout-features='*' --unicodes=$vietnameseUni

__CSS="\
/* Latin Basic, as defined by Google Fonts */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  src: url('fonts/$latinBasicFile') format('woff2');
  unicode-range: $latinBasicUni;
}

/* Latin extended, for diacritics in font which are not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  src: url('fonts/$latinExtFile') format('woff2');
  unicode-range: $latinExtUni;
}

/* Vietnamese glyphs not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  src: url('fonts/$vietnameseFile') format('woff2');
  unicode-range: $vietnameseUni;
}
"