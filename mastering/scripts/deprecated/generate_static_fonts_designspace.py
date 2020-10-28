import csv
import os
from fontTools.designspaceLib import DesignSpaceDocument

"""
Read designspace file, replace family and style names according to instance_names.csv
based on https://github.com/arrowtype/recursive/blob/master/mastering/data/write_ps_mapping_names.py
2020_01_07 Benedikt Bramboeck, Alphabet
"""

doc_paths = ["./sources/Roman/Fraunces.designspace", "./sources/Italic/FrauncesItalic.designspace"]

names = {}
with open("./mastering/data/instance_names.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names[(row["Var Instance Family Name"],
               row["Var Instance Style Name"])] = (row["postscript"],
                                                   row["Static Family Name"],
                                                   row["Static Style Name"])

for path in doc_paths:
    base, extension = os.path.splitext(path)

    doc = DesignSpaceDocument()
    doc.read(path)
    for i in doc.instances:
        k = (i.familyName, i.styleName)
        ps, fm, sm = names[k]
        i.postScriptFontName = ps
        i.familyName = fm
        i.styleName = sm

    static_path = base + "_static" + extension
    doc.write(static_path)