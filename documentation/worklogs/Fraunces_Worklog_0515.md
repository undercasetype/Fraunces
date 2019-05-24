# Fraunces Worklog: May 15th

Today, I turned my attention to starting to address spacing problems. I've been very loose with spacing up till now, and I think it's creating unnecessary inconsistencies (especially with similar characters i.e. e o c). So I spent today setting up groups for the Roman & Italic. I'm sure this will come in handy down the road for kerning everything as well.

I then wrote a quick script to copy groups from one font to another (scripts/copy-groups-font-to-font.py).

Then, I took a a simple script from the Robofont site that uses the groups, and updates the side bearings for all glyphs based on the group names (scripts/adjust-spacing-based-on-groups.py). This script is pretty rough, and I think I'll need to figure out a way of seeing the changes it is making/suggesting before committing to the new spacing. 