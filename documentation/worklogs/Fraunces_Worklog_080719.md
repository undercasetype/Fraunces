# Fraunces Production Notes – August 7th – Spencer

## Discrepencies in Widths

Yesterday, I generated animated gifs that show changes across axes in the Roman and Italic. I did this to demonstrate the axes, but noticed immediately that the rates of change in width were inconsistent between the two styles. 

I wonder if there is a way to measure these rates of change, and flag problems. First, I should probably check and see if an extension already exists for these comparisons. If not, I'm imagining a script that runs some sort of report, that gives a detailed assesment (character to character?) of rates of change, and flags outliers (glyphs whose rate of change is too little or too great in comparison to the average). The point of this is to see that rates of change are happening consistently across styles, but potentially this script could work master to master. Maybe that's a better starting point.

So here's how I envision the script working:

	– Take two masters, and use one master as the base to compare.
	– Go through, and compare the width of each glyph (minus sidebearings) in each master.
	– Divide those two numbers to return a percentage (rate of change)
	– Organize those rates of change from most to least (maybe color code the output for quick visual reference?)

I think this is a great starting point, and once I have this figured out, I can then worry about comparing multiple masters, and then multiple styles.

So far, I have the script creates an ordered output, with a filter Sensitivity. The output looks like this:

```Glyph-to-glyph comparison between Fraunces Light OpMin and Fraunces Black OpMin with a filterSensitivity of +-15:
['O: -25%', 'N: -19%', 'G: -19%', 'o: -16%', 'm: -16%', 'r: 17%', 'i: 30%', 'l: 30%', 'f: 30%', 'dotlessi: 30%', 't: 41%', 'I: 58%']```

Here, this tells me that the width of the O changes the least, and the width of the I changes the most. 
