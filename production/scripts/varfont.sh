#!/bin/bash
#!/Users/Cadmon/env/bin python

# This shell script is for building a variable font. 
# First, I want the script to run Stephen's varfont-prep.py. 
# In the new folder it creates, I want it to fontmake with the
# .designspace file that is in there.

# What are the arguments this script should take? The path of the first .designspace file.

echo "Enter the path for the varfont-prep.py file:"
read VFPREPPATH
#echo "Enter the path for the .designspace file:"
#read ds_path
#echo "You entered $ds_path for the file path."

roboFont --pythonpath -p $VFPREPPATH
