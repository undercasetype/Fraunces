# Fraunces Production Notes – August 7th – Spencer

## Discrepencies in Widths

Yesterday, I generated animated gifs that show changes across axes in the Roman and Italic. I did this to demonstrate the axes, but noticed immediately that the rates of change in width were inconsistent between the two styles. 

I wonder if there is a way to measure these rates of change, and flag problems. First, I should probably check and see if an extension already exists for these comparisons. If not, I'm imagining a script that runs some sort of report, that gives a detailed assesment (character to character?) of rates of change, and flags outliers (glyphs whose rate of change is too little or too great in comparison to the average). The point of this is to see that rates of change are happening consistently across styles, but potentially this script could work master to master. Maybe that's a better starting point.

## Master-to-Master Comparison, pt. 1

So here's how I envision the script working:

	• Take two masters, and use one master as the base to compare.
	• Go through, and compare the width of each glyph (minus sidebearings) in each master.
	• Divide those two numbers to return a percentage (rate of change)
	• Organize those rates of change from most to least (maybe color code the output for quick visual reference?)

I think this is a great starting point, and once I have this figured out, I can then worry about comparing multiple masters, and then multiple styles.

UPDATE: So far, I have the script create an ordered glyph output, with a filter Sensitivity. The output looks like this:

```
Glyph-to-glyph comparison between Fraunces Light OpMin and Fraunces Black OpMin with a filterSensitivity of +-15:
['O: -25%', 'N: -19%', 'G: -19%', 'o: -16%', 'm: -16%', 'r: 17%', 'i: 30%', 'l: 30%', 'f: 30%', 'dotlessi: 30%', 't: 41%', 'I: 58%']
```

## Master-to-Master Comparison, pt. 2

Now that I have the first part working, I want to see if I can have this script perform comparisons across all four masters of each style. The script so far looks at rates of change within the glyphs. What if I want to look at rates of change between masters? I suppose it could be as easy as looking at the meanTotal (the average percentage of change for all glyphs) that I figured out in the first script, and compare them to each other. So the output could be something like: 

```
thisMaster is XX% < or > than baseMaster meanTotal
within thisMaster, the following glyphs are xx% > or < the filterSensitivity.
```

A couple of things I'll have to do for this to work:

	• Have the user pick a base master to compare against.
	• Setup everything I've written so far as a function.

What I am shooting to get a rate for:

	• The rate of change on a given axis between the Max & Min should be roughly the same from Roman to Italic. If it isn't, what is a percentage that would bring those in line with each other.

So I've written the script as a function that allows you to specify a base master and a comparison master. By doing this, I can see that the Roman OpMin from Black to Light compresses 74%, and the Italic OpMin compresses 71%. Now that I have this information, I'm not sure what master should change. I could look at the rate of change between the Roman Black and Italic Black, and compare that against the Roman Light and Italic Light.