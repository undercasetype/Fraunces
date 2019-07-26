# Fraunces Production Notes – July 3rd – Spencer

Today, I began to plan the design space for Fraunces a little more in depth, specifically, I'm trying to tease out exactly how the Goofy axis will behave, and where the alt n,h,m,s characters fit in to this. Here is what I decided:

OpSz Axis affects
	– Contrast
	– x-height
	- tracking
	- width

Goofy axis affects (or specifically limits)
	- contrast
	- width

So, the Goofy axis will preserve whatever tracking and x-height changes the OpSz axis affects, and create a narrower range for contrast and width to change. Additionally, the alt leaning characters will not be directly controlled by any of these axis, only will exist as a rule that subs at small text sizes (16 pt and below?). Practically, this means that the non-leaning n, m, h, s won't be accessible by the user. I think the spirit of the typeface family *is* these leaning characters, and the only reason I'm introducing a normalized version is for easier long-form reading (small optical sizes)— that's it. 

## To Do with Flavia

– Look at Vertical Metrics (x-height, descender, ascender) across all masters and decide what those values should be. (maybe come up with spreadsheet to refer to later when designing?)

– finish drawing upper and lowercase characters, create goofy axis variants to fully test out design space

