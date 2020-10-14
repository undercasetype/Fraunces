import sys
from fontTools.ttLib import TTFont

def fix_naming(font_path):
    font = TTFont(font_path)
    italic = True
    if not "ITALIC" in font_path.upper():
        italic = False

    family_name = "Fraunces"
    if not italic:
        style_name = "Roman"
    else:
        style_name = "Italic"

    name_dict = {1: family_name,4: family_name, 6: f"{family_name}-{style_name}", 16: family_name, 17: style_name}
    
    if italic:
        name_dict[2] = style_name
        name_dict[4] = f"{family_name} {style_name}"

    for name_id, name_string in name_dict.items():
        font["name"].setName(name_string, name_id, 3, 1, 0x409)


    #get current ID3, rsplit on ; add id6
    old_name = font["name"].getName(3,3,1,0x409).toUnicode()
    new_name = f'{old_name.rsplit(";",1)[0]};{name_dict[6]}'
    font["name"].setName(new_name, 3, 3, 1, 0x409)
    font.save(font_path)
    font.close()
    print("Fixed NameIDs")

def main():
  for font_path in sys.argv[1:]:
    fix_naming(font_path)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()