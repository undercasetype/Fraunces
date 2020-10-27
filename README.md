# Fraunces Font Project

![alt text](documentation/img/HonkForWonkyFonts_revised.jpg "Honk For Wonky Fonts")

Fraunces is a display, "Old Style" soft-serif typeface inspired by the mannerisms of early 20th century typefaces such as [Windsor](http://fontreviewjournal.com/windsor/), Souvenir, and the Cooper Series.

This typeface family is still under development, and will be coming soon to Google Fonts.

## Variable Axes

Fraunces has the following axes:

Axis | Tag | Range | Default | Description
--- | --- | --- | --- | ---
Optical Size | opsz | 9pt to 144pt | 144pt | Labeled 9pt, 72pt, and 144pt in instances.
Weight | wght | 100 to 900 | 900 | Labeled Thin, Light, Regular, Semibold, Bold, and Black in instances.
Softness | SOFT | 000 to 100 | 100 | Labeled Sharp, Soft, and SuperSoft in instances.
Wonky | WONK | 0 to 1 | 1 | Binary axis controls substitution of "wonky" characters. Automatically substitutes when opsz > 18. Not listed in instances.

### Axis Definitions

#### `opsz` (Optical Size) Axis

The `opsz` axis ties together changes in contrast, x-height, spacing, and character widths. As `opsz` decreases, the x-height increases, spacing opens up, and the characters expand in width.

Additionally, mapping of axis values is placed in the AVAR table to create non-linear interpolation in the Variable font.

Many of the peculiar, wonky characteristics that are suitable for display usage are less desirable for more continuous reading. At certain smaller optical sizes (18px and less), the `wonk` axis is disabled (see below). 

![alt text](documentation/explanations/opsz_axis.gif "Changes in Optical Size")

#### `wght` (Weight) Axis

The `wght` axis spans Thin to Black. Nuff said.

![alt text](documentation/explanations/weight_axis.gif "Changes in Weight")

#### `SOFT` (Softness) Axis

The `SOFT` axis gives access to the softer, rounded forms that are available towards the Optical Min, but still retaining other Optical Sizing considerations, such as change in character width, spacing, tall ascenders, and shorter x-height

![alt text](documentation/explanations/goof_axis.gif "Changes in Softness")


#### `WONK` (Wonky) Axis

A binary axis that subsitutes `wonk` characters for more normalized characters, such as the leaning n/m/h in Roman, or the bulbous flags in the b/d/h/k/l of the Italic. In OTF or TTF instances, this can be implemented as an OpenType Stylistic Set.

![alt text](documentation/explanations/wonk_axis.gif "Changes in Wonk")

## Building the Fonts

From terminal, run the build script at `sources/build-all.sh`. Fonts output to `fonts/`.

NOTE: The first time you build, you will need to set up a virtual environment and install dependencies:

<details>
<summary><b><!-------->Setting up the build environment<!--------></b> (Click to expand)</summary>

### Set up the environment

To build, set up the virtual environment

```bash
python3 -m venv venv
```

Then activate it:

```bash
source venv/bin/activate
```

Then install requirements:

```bash
pip install -U -r requirements.txt
```

And finally, give the build scripts permission to run/execute (you can copy & paste, then run both lines in the terminal at once):

```bash
chmod +x sources/**/*.sh
chmod +x mastering/make-github-release/**/*.sh
```

Now, you can run `sources/build.sh`!

</details>

### Build fonts

Once you have set up the environment (see above), you can build fonts & prep releases!

When building a new version, add a version number (in the format of `1.001`) to update the UFO versions & version the fonts correctly. If you aren’t sure what version you should be building, check the number of the latest release in https://github.com/undercasetype/Fraunces/releases, then increment by `.001`. If you leave out the version number, it will just build with the same version number that already exists in the UFO sources.

To build variable and static fonts, plus make woff2s, use `build-all.sh`. This takes awhile (most of the time is taken up by building TTF & OTF static fonts).

```bash
sources/build-all.sh 1.000 # optional: place your desired version number as an argument
```

If you just want to build variable fonts, use `build.sh`:

```bash
sources/build-scripts/build-vf.sh 1.000 # optional: place your desired version number as an argument
```

To build only the static fonts (these are secondary to the variable fonts, so you can’t set the version numbers in this script), use `build-statics.sh`:

```bash
sources/build-scripts/build-statics.sh
```

## Production Notes

If you are doing any work on this repo, please read the production notes [here](https://github.com/undercasetype/Fraunces/tree/master/sources).

If you are looking for notes on making GitHub Release packages, see [mastering/README.md](mastering/README.md).
