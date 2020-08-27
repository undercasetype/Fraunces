# Production Notes

### Software

The following software and scripts was used in the production of this typeface family:
* [Robofont (v3)](https://robofont.com/)
* [GlyphConstruction](https://github.com/typemytype/GlyphConstruction)
* [MetricsMachine](https://extensionstore.robofont.com/extensions/metricsMachine/)
* [Scale & Interpolate](https://github.com/undercasetype/Fraunces/blob/master/production/scripts/ScaleAndInterpolate.py)

#### Interpolating Masters

The script `production/scripts/ScaleandInterpolate.py` was used to generate the following masters:

– 144pt S100 Light
– 144pt S100 Light Italic
– 144pt S100 Black
– 144pt S100 Black Italic
– 9pt S000 Light
– 9pt S000 Light Italic
– 9pt S000 Black
– 9pt S000 Black Italic

The recipes for those masters are to be found in `sources/ScaleAndInterpolate_Recipes.xlsx`. A great deal of manual corrections were required after generating the masters, so **DO NOT!!** use this script to overwrite these masters, only for future expansions of the design space (e.g. width axis).

#### Mounting Accents

GlyphConstruction was used in the mounting of accents. All GlyphConstruction files are located at `production/accents/`. A moderate amount of manual corrections were required after building the combined characters, so be sure to 

### Additional Production Scripts

In 	`production/scripts/` are additional Python scripts used in the production of this font. 