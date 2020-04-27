import os
from plistlib import dump as plDump

import fontTools
from fontTools.designspaceLib import DesignSpaceDocument
from statmake.lib import apply_stylespace_to_variable_font
from statmake.classes import Stylespace


def getStyleSpacePath(designspacePath):
    root, fileName = os.path.split(designspacePath)
    baseName = os.path.splitext(fileName)[0]
    newName = baseName + '.stylespace'
    stylespacePath = os.path.join(root, newName)
    return stylespacePath

def makeStyleSpace(designspace,path):
    # Style naming info
    styles = {
        "Optical Size":
        {
            9: "9pt",
            72: "72pt",
            144: "144pt"
        },
        "Weight":
        {
            100: "Thin",
            300: "Light",
            400: "Regular",
            600: "SemiBold",
            700: "Bold",
            900: "Black"
        },
        "soften":
        {
            0: "S000",
            50: "S050",
            100: "S100"
        },
        "wonk":
        {
            0:"0",
            1:"1"
        },
    }
    italic = False
    if "ITALIC" in designspace.filename.upper():
        italic = True
    axes = []
    for axis in designspace.axes:
        a = {}
        a["name"] = axis.name
        a["tag"] = axis.tag
        locations = []
        if axis.name == "Optical Size":
            for value, name in styles["Optical Size"].items():
                locations.append({"name": name, "value": value})
        elif axis.name == "Weight":
            for value, name in styles["Weight"].items():
                if value != 400:
                    locations.append({"name": name, "value": value})
                else:
                    locations.append({"name": name,
                                        "value": value,
                                        "linked_value": 700,
                                        "flags": ["ElidableAxisValueName"]
                                        })
        elif axis.name == "soften":
            for value, name in styles["soften"].items():
                locations.append({"name": name, "value": value})
        elif axis.name == "wonk":
            for value, name in styles["wonk"].items():
                locations.append({"name": name,
                                    "value": value,  
                                    "flags": ["ElidableAxisValueName"]})

        a["locations"] = locations
        axes.append(a)

    a = {}
    a["name"] = "Italic"
    a["tag"] = "ital"
    locations = []
    if italic:
        name = "Italic"
        value = 1
        linked_value = 0
        flags = []
    else:
        name = "Roman"
        value = 0
        linked_value = 1
        flags = ["ElidableAxisValueName"]
    locations.append({"name": name,
                        "value": value,
                        "linked_value": linked_value,
                        "flags": flags
                    })
    a["locations"] = locations
    axes.append(a)

    stat = {"axes": axes}
    with open(path, 'wb') as fp:
        plDump(stat, fp, sort_keys=False)

def add_STAT(designspacePath,fontPath, stylespacePath=None):
    if stylespacePath is None:
        stylespacePath = getStyleSpacePath(designspacePath)
    ds = DesignSpaceDocument.fromfile(designspacePath)
    
    makeStyleSpace(ds, stylespacePath)

    if stylespacePath is not None:
        print("Adding STAT table")  
        additional_locations = ds.lib.get("org.statmake.additionalLocations",
                                          {})
        font = fontTools.ttLib.TTFont(fontPath)
        stylespace = Stylespace.from_file(stylespacePath)
        apply_stylespace_to_variable_font(stylespace,
                                          font,
                                          additional_locations)
        font.save(fontPath)

if __name__ == "__main__":
    import argparse
    description = "Adds STAT to variable font."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("designspacePath",
                        help="The path to a designspace file")
    parser.add_argument("font",
                        help="Path to font file")
    parser.add_argument("-s", "--stylespace",
                        help="Path to the stylespace file")
    args = parser.parse_args()
    designspacePath = args.designspacePath
    fontPath = args.font
    stylespacePath = args.stylespace

    add_STAT(designspacePath, fontPath, stylespacePath=stylespacePath)