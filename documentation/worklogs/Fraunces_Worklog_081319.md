# Fraunces Worklog – August 13th – Spencer

##Problem:

Across the 8 masters (4 for each styles), the characters widths, and average widths of the masters fluctuate. This leads to different rates of change in the Roman and Italic across the different axes. Ideally, these masters should synchronize, and change at roughly the same rate.

Currently, I wrote a script that compares these rates of change, and gives me an average percentage of change between 2 masters. 

These numbers aren't particularly useful at the moment, because I'm not sure which masters need to change. If the rate of change between Light Italic Opmin/Black Italic Opmin is greater than the Roman counterpart, which of the two masters do I change? Do I normalize one? Normalize both? 

Looking just at glyph widths, it stands to reason that certain glyphs can only add weight to the outside (I, i, l), whereas others can add more weight to their interiors (O, G, C). 

Just looking at the numbers for the Romans to the Italics, the Italic compresses less in the Optical Size axis, and compresses more in the Weight axis. Potentially confusing the situation is that it could be a width problem, or weight problem, or a spacing problem, or all three. Additionally, it could be a problem with individual glyphs, or the entire master.

I suppose it makes the most sense to start by correcting individual glyphs, then overall masters. 

How can I set this up to generate a report that is visually useful for me? Right now, I'm looking at the average rate of change between the masters. What if I looked at the average amount of change per glyph, and compared those numbers from Roman to Italic? Start with a basic glyph-to-glyph comparison, and see how the numbers compare.

In order to normalize, I need to understand how that normalization occurs. Is there a "normal" to normalize to? I.e. Italic should be normalized to Roman, and all glyphs should be normalized to the master average?? How do the exceptions I outlined above fit into this?

Additionally, how do I separate the problems with spacing vs. width vs. weight? It all feels very intermingled and messy at the moment. Am I overthinking this?

In a very broad picture way, normalization is either:

– Normalize THIS to THAT

– Normalize THIS and THAT

There could be groups for normalization, similar to how there are groups for kerning and metrics. I.e. these letter shapes should behave roughly the same as these letter shapes.

## Idea for SpaceMachine

With character groups and master groups, normalize using 1 of 2 settings, normalize across spacing, widths, or weight.

What if there were a way to extrapolate a width axis from the existing information, and then normalize based on that information?? This could be a way of preparing all the current masters for a future width axis expansion. 