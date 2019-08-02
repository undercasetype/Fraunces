# Fraunces Production Notes – August 2nd – Spencer

## Finished Test Word

This week, Flavia and I finished drawing the test word HAMBURGEFONTSIV in upper and lowercase, for all Roman and Italic masters.

I also spent a good part of the week refining the proof doc scripts to look at spacing strings for each master, character to character comparisons of masters with Beta builds, and longer paragraph settings and 3 optical sizes. 

Flavia is going to go through the proof docs and write down all adjustments and corrections that she thinks need to be made. I will do the same.

After these corrections, I will then interpolate the masters to be used for the Goofy axis. I started testing this idea this afternoon, and I think it's working rather well (proof doc folder 080219). 

## Non-Linear Optical Size Interpolation

In the proof docs, I was noticing that the OpMid sizes were leaning more towards the OpMin than I would like (not enough contrast!). I found [this example of mapping that allows for Non-Linear interpolation](https://github.com/fonttools/fonttools/edit/master/Tests/varLib/data/BuildAvarEmptyAxis.designspace). As far as I can tell, this information is then put in the avar table, [which I learned a little about here](https://docs.microsoft.com/en-us/typography/opentype/spec/avar).

I tested this out in the proofs for 080219 and it works beautifully! 

## Next Steps

– Incorporate adjustments/corrections from latest proofs
– Build out Goofy axis for testing
