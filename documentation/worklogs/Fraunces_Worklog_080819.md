# Fraunces Production Notes – August 7th – Spencer

## Demonstration of Goofy Axis

The following animated gifs and images will demonstrate how the Goofy axis behaves across change in OpSz and Wght. For more extensive proofs of the Goofy Axis, [see the PDF's here](https://github.com/sponcey/Fraunces/tree/master/documentation/proofs/080819/PDFs). Variable Fonts of the Goofy Axis are [available here](https://github.com/sponcey/Fraunces/tree/master/documentation/proofs/080819/fonts).

### Goofy Axis Deltas

The Goofy Max decreases the contrast, and slight change in width that we see in the Optical Sizing, however retains the lower x-height, tighter spacing, and long ascenders/descenders.

The changes in the Goofy Axis are much more noticeable in the OpSz max, since this axis is intended to give the user access to the "juicier" side of the typeface, while still retaining certain OpSz considerations.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/goofyDeltas.png "Goofy Deltas")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/goofyDeltas_Italic.png "Italic Goofy Deltas")

Below is an example of changes across the Goofy Axis for a Min Weight, Mid Weight, and Max Weight.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/goofyChange.gif "Changes across Goofy Axis")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/goofyChange_Italic.gif "Changes across Italic Goofy Axis")

### Non-Linear OpSz Interpolation

The Goof Min is essentially the unchanged Optical Max masters that we see currently in the design space. I've incorporated [non-linear axis mapping](https://docs.microsoft.com/en-us/typography/opentype/spec/avar) for OpSz in the .designspace file, so that the delicate features are retained for a larger size range.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/nonlinear.gif "Non Linear") ![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/linear.gif "Linear")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/nonlinear_italic.gif "Non Linear Italic") ![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/linear_italic.gif "Linear Italic")

This will allow for a more harmonized appearance of text at various OpSz's.

### OpSz Min Rules/Substitutions

Currently, a rule is set up so that below 18px, the following glyphs substitute for a more normalized character. I've made a design decision to seperate these rules from the Goofy Axis, mainly because I don't want these subsitutions be activated at larger sizes, only to help deal with smaller optical sizes.

Roman: h, n, m, s

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/rules_comparisons.png "Roman Subs")

Italic: b, d, h, l, k, v

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/rules_comparisons_italic.png "Italic Subs")

## To-Do

For the Goofy axis to work properly, we will need to figure out the true interpolations for the lowercase of the OpMax Goof Max in Light and Black. In the past, Flavia and I would have used UFOStretch, which unfortunately doesn't work with ufo3 files. Currently, we scale the lowercase to match the OpMax Goof Min heights, move the ascender/descenders, and compress the tracking.

However, we will worry about this later, since at this stage, we've built this purely as proof of concept.

	– Does it make sense to call it the "Goofy" axis? Would "Contrast" be more succinct?
	- How can we toggle substitutions of "wonk" without the Goofy axis?