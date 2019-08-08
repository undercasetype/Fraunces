# Fraunces Production Notes – August 7th – Spencer

## Demonstration of Goofy Axis

The following animated gifs will demonstrate how the Goofy axis behaves across change in OpSz and Wght. 

### Change in OpSz and Font Size, fixed Goofy Min

The Goof Min is essentially the unchanged Optical Max masters that we see currently in the design space. I've incorporated [non-linear axis mapping](https://docs.microsoft.com/en-us/typography/opentype/spec/avar) for OpSz in the .designspace file, so that the delicate features are retained for a larger size range.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/OpSzChange_wghtMax_goofMin.gif "OpSz Change, Wght Max Goof Min")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/OpSzChange_wghtMin_goofMin.gif "OpSz Change, Wght Min Goof Min")

### Change in OpSz and Font Size, fixed Goofy Max

The Goofy Max decreases the contrast, and slight change in width that we see in the Optical Sizing, however retains the lower x-height, tighter spacing, and long ascenders/descenders.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/OpSzChange_wghtMax_goofMax.gif "OpSz Change, Wght Max Goof Max")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/OpSzChange_wghtMin_goofMax.gif "OpSz Change, Wght Min Goof Max")

### Change In Goofy Axis, fixed OpSz Min

In the OpMin, the changes across the Goofy Axis are much less noticeable, since the Optical Size considerations at 9px are far more demanding.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/GoofyChange_opMin_wghtMin_fixedSize.gif "Goofy Change, Op Min Wght Min")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/GoofyChange_opMin_wghtMax_fixedSize.gif "Goofy Change, Op Min Wght Max")

### Change in Goofy Axis, fixed OpSz Max

The changes in the Goofy Axis are much more noticeable in the OpSz max, since this axis is intended to give the user access to the "juicier" side of the typeface, while still retaining certaing OpSz considerations.

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/GoofyChange_opMax_wghtMin_fixedSize.gif "Goofy Change, Op Max Wght Min")

![alt text](https://github.com/sponcey/Fraunces/blob/master/documentation/proofs/080819/GoofyChange_opMax_wghtMax_fixedSize.gif "Goofy Change, OpMax Wght Max")
