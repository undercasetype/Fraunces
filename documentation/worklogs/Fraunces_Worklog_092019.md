# Fraunces Worklog - September 20th - Spencer

There was *alot* of planning this week. I talked to Andy Clymer on Friday, who gave us some great feedback about how to construct the Goofy Axis. I also talked with Kabisa, who will be handling the digital specimen, and Alphabet, who will be working on the designspace files and mastering.

## Goofy Axis Recipe

Andy's biggest piece of feedback was coming up with a clear recipe for how the Goofy Axis masters are constructed, and possible doing more at the OpMin to make sure the Goofy extremes have a clear distinction. Andy started writing a script that allows us to generate an interpolation/extrapolation (/documentation/scripts/ScaleAndAdjust.py). My hope was that I could get ScaleFast to do this for us, but for the last couple of months, have not been able to get it to launch no matter what I throw at it. I think this will be a great roadblock to clear. I started recipes here (/sources/designspace_explorations/GoofyRecipes.md) We will most likely wait till the beginning of November once the rest of the character set is solid to bring in a third person to make corrections to these Goofy masters.

## Mastering Chat w/ Alphabet

We've been having issues with the .designspace files we've generated from Superpolator. At the OpMin (9.0) in different browsers, it defaults to different areas of the designspace. Additionally, in one browser, the avar mapping that should only be applied to the OpSz seems to be applying to the Weight axis as well.

In addition to this, figuring out naming & instances, Alphabet is happy to debug Fraunces in order to pass FontBakery requirements. This will be a big weight off my shoulders :)

## Refining Core Roman & Italic

I spent this week drawing the remaining numbers and punctuation for Roman, and making refinements to the Italic. Flavia is currently working her way back over the Italic masters and simplifying the point structure in the Italic. This is time consuming (I wish I had drawn better in the first place), but it's best to catch this now before the character set expands drastically in the next month or two. I will generate proof docs as soon as we have working/interpolatable files, and will include demos of the Goofy Axis with the script Andy has provided.

## Specimen Updates

Doug is currently at work on the print specimen, aiming for a finish date of mid-November. We will have a review with Google at the end of the month.

I talked with Kabisa last week about their availability and interest in designing the digital specimen. They got back to me a few days ago and confirmed their interest. They will be handling concept, design, and implementation, and will start most likely beginning of November. I'm excited to see what they come up with :)

## End of Week Conclusion

Overall, I'm feeling optimistic about having this completed by the end of the year. There is a lot to do, but with certain parts of this puzzle in the right hands, I think it will come together in a great way.

-------------------

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