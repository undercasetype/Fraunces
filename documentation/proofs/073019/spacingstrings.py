import datetime

now = datetime.datetime.now()
newFileName = "paragraph_proofs" + now.strftime("%Y_%m_%d-%H_%M_%S")

# Text from external source
path = "/Users/Cadmon/Documents/GitHub/Fraunces/documentation/proofs/073019/hamburgefontsiv_spacingstring.txt"
strings = open(path, "r", encoding="utf-8")
stringstext = strings.read()
strings.close()
#stringstext = stringstext.split("\n")

print(stringstext)

# Variables
fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10

## Start of Script ##
for x in range(0,10,1):
    newPage("TabloidLandscape")
    # for y in range(0,7,1):
    font("Fraunces", 50)
    textBox(stringstext, (margin,margin,width(),height()))