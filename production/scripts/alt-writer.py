## Alt Writer for .designspace and OpenType

f = CurrentFont()

altlist = []
glist = []

for g in f:
    if ".alt" in g.name:
        altlist.append(g.name)
        
for g in f:
    if ".alt" in g.name:
        glist.append(g.name[:-4])
                
altlist.sort()    
glist.sort()


# Writer for OpenType

alts_on = ""

alts_off = ""

for g in altlist:
    alts_on += "%s " % g 
    
for g in glist:
    alts_off += "%s " % g   
    
print("@alts_on = [ %s];" % alts_on)
print("@alts_off = [ %s];" % alts_off)

for g in altlist:
    print("<sub name='%s' with='%s' />" % (g[:-4],g))

# Writer for .designspace