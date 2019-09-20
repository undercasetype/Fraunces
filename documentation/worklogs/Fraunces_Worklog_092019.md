# Fraunces Worklog - September 20th - Flavia

## Refinements

For the last couple of weeks I was working on refining the Roman masters. The OptMin got more work done, but OptMax needs a second look. And more tests overall to check texture across all "instances".

Today I started the same clean up in the Italics, starting from the BlackOptMin and got around some of the lowercase. And then made changes to all masters to keep the point structure compatible. 

Things I am looking at while making this fine tuning:

>> serif construction/ length: since the upm was bumped to 2000, we can definitely draw them in a better way. And make sure they have the same shape across the board. I notice in the italics the exist & entry strokes/ flags were (are) varying a lot.

>> vertical metrics: check if cap Height/ ascender/ descender values/ positions are the same in all masters. And x-height/ overshoot is consistent within the same weights.

>> proportions: see if something is jumping out in real text.
>> weight consistency (specially in the Light/ Hairline): same as above.
>> italic angle: same as above.


## Test Installing Roman & Italics at the same time.

The trick I found to make this work is to rename both masters as following:

Roman: 
Family name: Fraunces/ Style name: Black/ Full name: Fraunces Black
Italic: 
Family name: Fraunces/ Style name: Black Italic / Full name: Fraunces Black Italic

I took the OptMin/Max out of the naming, so it's best to work in one axis per time.
Also take a look at the Postscript table (in Font info) to see if the names match.
After making corrections/ proofing, change the name back to the original.