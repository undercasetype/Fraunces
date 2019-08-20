# Fraunces Worklog - August 20th - Spencer

## Corrected Widths

In the OpMax and Min of the Italic Light, the masters were much more compressed on average compared to the Roman. I went through and normalized the widths, and they now feel more in line with the rates of change in the Roman from OpMin to OpMax.

However, after making this change and generating new VF files, the WONK axis doesn't seem to be working in the Roman. It's defaulting to the substituted characters. Very frustrating! I'm not sure what is happening here, since I'm using the same settings used to set up the wonk axis in the Italic.

Note for Flavia: I spent quite a bit of time going through and adding points to make all the masters in the Roman compatible, based on changes that were made last week to the OpMin's. Moving forward, I think if any points are added or subtracted from a master, we should do it for all 4 masters at the same time. Otherwise it can cause headaches with interpolations, because prepolator does not seem to catch these small changes.

## Entry/Exit Strokes in Italic Min

The entry/exit strokes in the Italic Min maybe too long. They start looking kind of noodly and distracting. Maybe a better comparison is to the length of the serif in the Roman?

UPDATE: I shortened the entry/exit strokes, and it seems to have significantly improved the texture in the light opmin, far less noodly feeling. There are two PDF's in the proofs folder for 082019 that show the differences.