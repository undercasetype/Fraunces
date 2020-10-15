"""
    Fix issues in name table that are results of generating fonts from UFOs in a designspace.

    Examples:
    - Set Name 2 to "Italic" in italic fonts
"""

import sys, re, unicodedata, os
import fontTools.ttLib
# from fontbakery.parse import style_parse
from fontbakery.profiles.googlefonts_conditions import expected_style

#file = "/Users/yanone/Projekte/Google/Onboarding/piazzolla/fonts/Piazzolla/variable/ttf/Piazzolla-Italic[opsz,wght].ttf"#sys.argv[1]
file = sys.argv[1]
ttFont = fontTools.ttLib.TTFont(file)


RIBBI_style = [
    "Regular",
    "Italic",
    "Bold",
    "Bold Italic"
]


fsSelection_values = {
    "Regular": 64,
    "Italic": 1,
    "Bold": 32,
    "Bold Italic": 33,
}

macStyle_values = {
    "Regular": 0,
    "Italic": 2,
    "Bold": 1,
    "Bold Italic": 3,
}


def return_font_file_full_path(folder, filename):
    font_file_full_path = f"{folder}/{filename}"
    return font_file_full_path

def return_filename_no_extension(filename):
    filename_no_extension = os.path.basename(filename).split(".")[0]
    return filename_no_extension

# should work well if the designspace has correct naming
def return_familyname(font):
    familyName = ttFont["name"].getName(nameID=16,  platformID=3, platEncID=1, langID=0x409 )

    # If the font is RIBBI, name 16 doesn’t exist, and FontTools returns None (as a NoneType)
    if familyName == None:
        familyName = ttFont["name"].getName(nameID=1,  platformID=3, platEncID=1, langID=0x409 )

    return str(familyName)

def return_stylename(filename):
    stylename = filename_no_extension.split("-")[1]
    stylename = stylename.replace("pt", "pt ")
    return stylename

def split_name(string):
    splitted_name = re.findall('[A-Z][^A-Z]*', string)
    return splitted_name

def remove_spaces(string):
    string = "".join(string.split(" "))
    return string


def return_nameID_1(familyname, stylename):
    if stylename in RIBBI_style:
        nameID1 = familyname
    else:
        if "Italic" in stylename:
            stylename_without_italic = stylename.replace(" Italic", "")
            nameID1 = f"{familyname} {stylename_without_italic}"
        elif "Regular" in stylename:
            stylename_without_regular = stylename.replace(" Regular", "")
            nameID1 = f"{familyname} {stylename_without_regular}"
        else:
            nameID1 = f"{familyname} {stylename}"
    return nameID1

def return_nameID_2(stylename):
    if stylename in RIBBI_style:
        nameID2 = stylename
    else:
        if "Italic" in stylename:
            nameID2 = "Italic"
        else:
            nameID2 = "Regular"
    return nameID2

def is_RIBBI(stylename):
    if stylename in RIBBI_style:
        return True
    else:
        return False


# Variable Font
if 'fvar' in ttFont:

    # Sub family name
    style = expected_style(ttFont)

    for name in ttFont['name'].names:
        if name.nameID == 2:
            name.string = style.win_style_name
        if name.nameID == 17:
            name.string = style.typo_style_name

    familyName = return_familyname(ttFont)

    ttFont["name"].setName( string=familyName,  nameID=1,  platformID=3, platEncID=1, langID=0x409 )
    ttFont["name"].setName( string=familyName,  nameID=1,  platformID=3, platEncID=1, langID=0x409 )


    # TODO: check if fixing this in the UFOs solves the problem
    if '-Italic' in file:
        ttFont['head'].macStyle |= 1 << 1 # Set  bit 1
        ttFont['OS/2'].fsSelection |= 1 << 0 # Set bit 0 (Italic)
        ttFont['OS/2'].fsSelection = ttFont['OS/2'].fsSelection & ~(1<<5) # Unset bit 5 (Bold)
        ttFont['OS/2'].fsSelection = ttFont['OS/2'].fsSelection & ~(1<<6) # Unset bit 6 (Regular)


# Static Font
else:

    filename_no_extension = return_filename_no_extension(file)
    # familyname = return_familyname(file)
    familyname = return_familyname(ttFont)
    temp_stylename = return_stylename(file)

    if temp_stylename != "Italic":
        stylename = temp_stylename.replace("Italic", " Italic")
    else:
        stylename = temp_stylename

    print(familyname, stylename)

    nameID1  = return_nameID_1(familyname, stylename)
    nameID2  = return_nameID_2(stylename)
    nameID4  = f"{familyname} {stylename}"
    nameID6  = f"{remove_spaces(familyname)}-{remove_spaces(stylename)}"
    nameID16 = familyname
    nameID17 = stylename
    nameID18 = nameID4

    # Remove 16, 17, 18
    try:
        ttFont["name"].removeNames(nameID=18)
        ttFont["name"].removeNames(nameID=17)
        ttFont["name"].removeNames(nameID=16)
    except:
        pass

    print('nameID1: ',  nameID1)
    print('nameID2: ',  nameID2)
    print('nameID4: ',  nameID4)
    print('nameID6: ',  nameID6)
    print('nameID16: ', nameID16)
    print('nameID17: ', nameID17)
    print('nameID18: ', nameID18)
    

    ttFont["name"].setName( string=nameID1,  nameID=1,  platformID=3, platEncID=1, langID=0x409 )
    ttFont["name"].setName( string=nameID2,  nameID=2,  platformID=3, platEncID=1, langID=0x409 )
    ttFont["name"].setName( string=nameID4,  nameID=4,  platformID=3, platEncID=1, langID=0x409 )
    ttFont["name"].setName( string=nameID6,  nameID=6,  platformID=3, platEncID=1, langID=0x409 )
    ttFont["name"].setName( string=nameID18,  nameID=18,  platformID=3, platEncID=1, langID=0x409 )

    if not is_RIBBI(stylename):
        ttFont["name"].setName( string=nameID16, nameID=16, platformID=3, platEncID=1, langID=0x409 )
        ttFont["name"].setName( string=nameID17, nameID=17, platformID=3, platEncID=1, langID=0x409 )

    # Fix fsSelection and macStyle
    nameID_2 = ttFont["name"].getName(nameID=2, platformID=3, platEncID=1).toStr()
    if is_RIBBI(stylename) == True:
        ttFont["OS/2"].fsSelection = fsSelection_values[nameID_2]
        ttFont["head"].macStyle = macStyle_values[nameID_2]
    else:
        if nameID_2 == "Regular":
            ttFont["OS/2"].fsSelection = fsSelection_values["Regular"]
            ttFont["head"].macStyle = macStyle_values["Regular"]
        else:
            ttFont["OS/2"].fsSelection = fsSelection_values["Italic"]
            ttFont["head"].macStyle = macStyle_values["Italic"]


ttFont.save(file)
