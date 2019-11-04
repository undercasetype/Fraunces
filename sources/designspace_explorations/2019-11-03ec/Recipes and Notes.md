Fraunces goofy and opsz axis explorations:

I wanted to try repurposing the current OpMin GoofyMin masters as OpMin GoofyMax and generating new higher contrast OpMin Goofy masters. This involved generating new masters and then swapping filenames and font info. These are the steps:

1. Generate new OpMin GoofyMax masters with higher contrast.
2. Delete "GoofyMax" from font info and filename in OpMin GoofyMax masters.
3. Add "GoofyMax" to font info and filename in OpMin GoofyMin masters.

Here are the formulas used for step 1 to generate the new OpMin GoofyMax masters with ScaleAndInterpolate.py in ~/documentation/scripts/. **I generated these _before_ swapping the filenames.** I'm keeping the GoofyMax OpMax formulas in here even though I am not changing them, so that everything is still in one place.

## ROMAN ##

# GoofyMax OpMax Black: LightOpMin & Black OpMin

Caps
Scale Horizontal: 93
Scale Vertical: 100
Interpolate Horizontal: 100
Interpolate Vertical: 95
Units of Tracking: -30

Lowercase
Scale Horizontal: 85
Scale Vertical: 92
Interpolate Horizontal: 106
Interpolate Vertical: 103
Units of Tracking: -20

# GoofyMax OpMax Light: LightOpMin & Black OpMin

Caps
Scale Horizontal: 93
Scale Vertical: 100
Interpolate Horizontal: -2
Interpolate Vertical: -4
Units of Tracking: -40

Lowercase
Scale Horizontal: 85
Scale Vertical: 92
Interpolate Horizontal: 2
Interpolate Vertical: 0
Units of Tracking: -30

# GoofyMax OpMin WeightMax: Black OpMax & Black OpMin ~~LightOpMin & Black OpMin~~

Caps
Scale Horizontal: 100
Scale Vertical: 100
Interpolate Horizontal: 50
Interpolate Vertical: 50
Units of Tracking: 0

Lowercase
Scale Horizontal: 103.6 _(based on height of /x)_
Scale Vertical: 103.6 _(based on height of /x)_
Interpolate Horizontal: 50
Interpolate Vertical: 50
Units of Tracking: 0

# GoofyMax OpMin WeightMin: Light OpMax & Light OpMin ~~LightOpMin & Black OpMin~~

Caps
Scale Horizontal: 100
Scale Vertical: 100
Interpolate Horizontal: 70
Interpolate Vertical: 70
Units of Tracking: 0

Lowercase
Scale Horizontal: 102.5 _(based on height of /x)_
Scale Vertical: 102.5 _(based on height of /x)_
Interpolate Horizontal: 70
Interpolate Vertical: 70
Units of Tracking: 0


## Italic ##

# GoofyMax OpMax Black: LightOpMin & Black OpMin

Caps
Scale Horizontal: 93
Scale Vertical: 100
Interpolate Horizontal: 100
Interpolate Vertical: 95
Units of Tracking: -30

Lowercase
Scale Horizontal: 85
Scale Vertical: 92
Interpolate Horizontal: 110
Interpolate Vertical: 103
Units of Tracking: -20

Skew: 2°

# GoofyMax OpMax Light: LightOpMin & Black OpMin

Caps
Scale Horizontal: 93
Scale Vertical: 100
Interpolate Horizontal: -2
Interpolate Vertical: -4
Units of Tracking: -40

Lowercase
Scale Horizontal: 85
Scale Vertical: 92
Interpolate Horizontal: 2
Interpolate Vertical: 0
Units of Tracking: -30

Skew: 2°

# GoofyMax OpMin WeightMax: Black OpMax & Black OpMin ~~LightOpMin & Black OpMin~~

Caps
Scale Horizontal: 100
Scale Vertical: 100
Interpolate Horizontal: 50
Interpolate Vertical: 50
Units of Tracking: 0

Lowercase
Scale Horizontal: 103.6 _(based on height of roman /x)_
Scale Vertical: 103.6 _(based on height of roman /x)_
Interpolate Horizontal: 50
Interpolate Vertical: 50
Units of Tracking: 0

Skew: 0°

# GoofyMax OpMin WeightMin: Light OpMax & Light OpMin ~~LightOpMin & Black OpMin~~

Caps
Scale Horizontal: 100
Scale Vertical: 100
Interpolate Horizontal: 70
Interpolate Vertical: 70
Units of Tracking: 0

Lowercase
Scale Horizontal: 102.5 _(based on height of roman /x)_
Scale Vertical: 102.5 _(based on height of roman /x)_
Interpolate Horizontal: 70
Interpolate Vertical: 70
Units of Tracking: 0

Skew: 0°
