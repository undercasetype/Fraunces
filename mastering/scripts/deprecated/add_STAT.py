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

def get_range(values, value):
    values = list(values)
    i = values.index(value)
    if values[i] == min(values):
        min_range = values[i]
        max_range = (values[i] + values[i+1]) / 2
    elif values[i] == max(values):
        min_range = (values[i-1] + values[i]) / 2
        max_range = values[i]
    else:
        min_range = (values[i-1] + values[i]) / 2
        max_range = (values[i] + values[i+1]) / 2

    return((min_range,max_range))

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
        "Softness":
        {
            0: "Sharp",
            50: "Soft",
            100: "SuperSoft"
        },
        "Wonky":
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
                v_range = get_range(sorted(styles["Optical Size"].keys()), value)
                locations.append({"name": name, "value": value, "range":v_range})
        elif axis.name == "Weight":
            for value, name in styles["Weight"].items():
                v_range = get_range(sorted(styles["Weight"].keys()), value)
                if value != 400:
                    locations.append({"name": name, "value": value, "range": v_range})
                else:
                    locations.append({"name": name,
                                        "value": value,
                                        "range": v_range,
                                        "linked_value": 700,
                                        "flags": ["ElidableAxisValueName"]
                                        })
                    # locations.append({"name": name,
                    #                     "value": value,
                    #                     "linked_value": 700,
                    #                     "flags": ["ElidableAxisValueName"]
                    #                     })
        elif axis.name == "Softness":
            for value, name in styles["Softness"].items():
                v_range = get_range(sorted(styles["Softness"].keys()), value)
                locations.append({"name": name, "value": value, "range": v_range})
        elif axis.name == "Wonky":
            for value, name in styles["Wonky"].items():
                if value != 1:
                    locations.append({"name": name, "value": value})
                else:
                    locations.append({"name": name,
                                    "value": value,  
                                    "flags": ["ElidableAxisValueName"]})

        a["locations"] = locations
        axes.append(a)

    a = {}
    a["name"] = "Italic"
    a["tag"] = "ital"
    locations = []

    name = "Italic"
    value = 1
    # linked_value = 0
    # flags = []
    locations.append({"name": name,
                      "value": value,
                    })

    name = "Upright"
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