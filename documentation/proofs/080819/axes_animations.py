scaleup = 2
    
axisValues = {"wghtMax": 1000, "wghtMin": 100, "goofMax": 100, "goofMin": 1, "opMax": 144, "opMin": 9}

def gifGenerator(axisMin, axisMax, fixAxis1, fixAxis2):
    rate = int((axisValues[axisMax]-axisValues[axisMin]) / 20)
    for x in range(axisValues[axisMax],axisValues[axisMin],-rate):
        newPage(1000*scaleup, 300*scaleup)
        fill(1,1,1)
        rect(0,0,width(),height())
        fill(0,0,0)
        if axisMin == "opMin":
            name = "OpSzChange"
            font("Recur Mono", 10*scaleup)
            text("Optical Size: %s, Weight = %s, Goofy = %s" % (x, axisValues[fixAxis1], axisValues[fixAxis2]), (10*scaleup,10*scaleup))
            fontVariations(opsz = x+0.1, wght = axisValues[fixAxis1], goof = axisValues[fixAxis2])
        if axisMin == "goofMin":
            name = "GoofyChange"
            font("Recur Mono", 10*scaleup)
            text("Optical Size: %s, Weight = %s, Goofy = %s" % (axisValues[fixAxis1], axisValues[fixAxis2], x), (10*scaleup,10*scaleup))
            fontVariations(opsz = axisValues[fixAxis1]+0.1, wght = axisValues[fixAxis2], goof = x)
        if axisMin == "wghtMin":
            name = "WghtChange"
            font("Recur Mono", 10*scaleup)
            text("Optical Size: %s, Weight = %s, Goofy = %s" % (axisValues[fixAxis1], x, axisValues[fixAxis2]), (10*scaleup,10*scaleup))
            fontVariations(opsz = axisValues[fixAxis1]+0.1, wght = x, goof = axisValues[fixAxis2])
        font("Fraunces", 80*scaleup)
        text("HAMBURGEFONTSIV", (50*scaleup,175*scaleup))
        text("hamburgefontsiv", (50*scaleup,60*scaleup))
    saveImage("%s_%s_%s.gif" % (name, fixAxis1, fixAxis2))
    
## Goofy Gifs    
#gifGenerator("goofMin", "goofMax", "opMin", "wghtMin")
#gifGenerator("goofMin", "goofMax", "opMax", "wghtMin")
#gifGenerator("goofMin", "goofMax", "opMin", "wghtMax")
#gifGenerator("goofMin", "goofMax", "opMax", "wghtMax")

## OpSz Gifs
#gifGenerator("opMin", "opMax", "wghtMin", "goofMin")
#gifGenerator("opMin", "opMax", "wghtMax", "goofMin")
#gifGenerator("opMin", "opMax", "wghtMin", "goofMax")
#gifGenerator("opMin", "opMax", "wghtMax", "goofMax")

## Wght Gifs
gifGenerator("wghtMin", "wghtMax", "opMin", "goofMin")
#gifGenerator("wghtMin", "wghtMax", "opMax", "goofMin")
#gifGenerator("wghtMin", "wghtMax", "opMin", "goofMax")
#gifGenerator("wghtMin", "wghtMax", "opMax", "goofMax")
