# Fraunces Font Project

![alt text](documentation/img/HonkForWonkyFonts.jpg "Honk For Wonky Fonts")

Fraunces is a display, "Old Style" soft-serif typeface inspired by the mannerisms of early 20th century typefaces such as [Windsor](http://fontreviewjournal.com/windsor/), Souvenir, and the Cooper Series.

This typeface family is still under development, and will be ready for initial release by early 2020.

## Variable Axes

Fraunces has the following axes:

Axis | Tag | Range | Default | Description
--- | --- | --- | --- | ---
Optical Size | opsz | 9 to 144 | 9 | Labeled 9, 72, and 144 in instances.
Weight | wght | 100 to 900 | 100 | Labeled Thin, Light, Regular, Semibold, Bold, and Black in instances.
Goofy | GOOF | 0 to 100 | 100 | Labeled G0, G50, and G100 in instances.
Wonk | WONK | 0 to 1 | 0.5 | Controls substitution of "wonky" characters. Automatically substitutes when opsz > 18. Not listed in instances.

### Weight Axis

The weight axis spans Thin to Black. Nuff said.

![alt text](documentation/explanations/weight_axis.gif "Changes in Weight")

### GOOF Axis

The "goofy" axis gives access to the chocolate-y, chunky forms that are available towards the Optical Min, but still retaining other Optical Sizing considerations, such as change in character width, spacing, tall ascenders, and shorter x-height

![alt text](documentation/explanations/goof_axis.gif "Changes in Goofy")

### Optical Size Axis

The optical size axis ties together changes in contrast, x-height, spacing, and character widths. As the optical size decreases, the x-height increases, spacing opens up, and the characters expand in width.

Additionally, mapping of axis values is placed in the AVAR table to create non-linear interpolation in the Variable Font.

Many of the peculiar, wonky characteristics that are suitable for display usage are less desirable for more continuous reading. At certain smaller optical sizes (18px and less), the WONK axis is disabled (see below). 

![alt text](documentation/explanations/opsz_axis.gif "Changes in Optical Size")


### WONK Axis

A binary axis that subsitutes "wonky" characters for more normalized characters, such as the leaning n/m/h in Roman, or the bulbous flags in the b/d/h/k/l of the Italic. In traditional instances of fonts, this will be implemented as a Stylistic Set.

![alt text](documentation/explanations/wonk_axis.gif "Changes in Goofy")
