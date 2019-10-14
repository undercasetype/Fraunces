'''Character Set Proofer'''
from time import gmtime, strftime

## GLOBAL VARIABLES ##

size('A4Landscape')

def drawFont(master):
    f = master
    g = CurrentGlyph()

    # main variables
    boxHeight = 70
    boxPaddingX = 0
    boxPaddingY = 20
    margin = 30
    pagenum = 1
    formatteddate = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # calculate scale
    s = float(boxHeight) / f.info.unitsPerEm

    # define page size
    pageWidth, pageHeight = width(), height()

    # calculate initial positions
    x = margin
    y = pageHeight - margin - boxHeight

    # draw glyph
    def drawglyph():
        xGlyph = xBox
        yGlyph = yBox - f.info.descender*s
        save()
        translate(xGlyph, yGlyph)
        fill(0)
        stroke(None)
        scale(s)
        drawGlyph(g)
        restore()
    
    # draw captions
    def drawcaptions():
        t = 12 # em size
        captionX = t
        captionW = width() - t*2
        captionH = t*2
    
        save()
        font('VulfMono-Regular')
        fontSize(t*.75)
        fill(0, 0, 0)

         # bottom caption
        captionY = 0
        captionBox = captionX, captionY, captionW, captionH
        textBox('%s • %s' % (f.info.familyName+" "+f.info.styleName, sectiontitle), captionBox, align='left')
        textBox('%s • Page %s' % (formatteddate, pagenum), captionBox, align='right')
    
    # Generates spacing strings as formatted list of strings    
    def stringgenerator():
        # TODO: Translate color values to HEX string to avoid comparing floats
        template = {
            #uppercase (red)
            (1.0, 0.0, 0.0, 1.0) : u"HH{}HH{}OO{}OO",
            #lowercase (yellow)
            (1.0, 1.0, 0.0, 1.0) : u"nn{}nn{}oo{}oo",
            #numerals (blue)
            (0.0, 0.0, 1.0, 1.0) : u"00{}00{}11{}11"
        }

        # Define results array
        results = []

        for name in f.keys():
            g = f[name]
            # Removed "if g and" because it was pulling out fractions for some reason?
            if g.unicode and g.mark and template[g.mark]:
                c = chr(g.unicode)
                # Append tuple of (color, glyph, template) to results
                results.append((g.mark, c , template[g.mark].format(c,c,c)))

        # Results now contains an array of Tuples of the form
        # [(color, glyph, template), ...]

        # Sort the results using tuple comparison function
        # which lexically sorts based off of ordinal position of
        # items in tuple.
        results.sort()

        # Iterate through array of Tuples
        # unpacking contents of Tuple into glyph and template, ignoring the color
        for (_, glyph, template) in results:
            print(u"{}\t{}".format(glyph,template))


    ## SECTION 1: CHARACTER SET ##

    sectiontitle = "Character Set"
    xBox, yBox = x, y
    drawcaptions()
    for i, glyphName in enumerate(f.glyphOrder):

        g = f[glyphName]
        boxWidth = g.width*s

        # jump to next line
        if xBox + boxWidth >= pageWidth - margin:
            xBox = x
            yBox -= boxHeight + boxPaddingY
            # jump to next page
            if yBox < margin:
                yBox = y
                newPage(pageWidth, pageHeight)
                drawcaptions()
                pagenum += 1

        # draw glyph cell
        stroke(None)
        fill(None)
        rect(xBox, yBox, boxWidth, boxHeight)
    
        stroke(None)
        fill(None)
        rect(xBox, yBox, boxWidth, boxHeight*1.2)
    
        if g.width == 0:
            continue
        else:
            drawglyph()
        # move to next glyph
        xBox += boxWidth + boxPaddingX
        
for f in AllFonts():
    drawFont(f)
    newPage()
    
    
    # ## SECTION 2: SPACING STRINGS ##

    # sectiontitle = "Spacing Strings"
    # newPage(pageWidth,pageHeight)
    # drawcaptions()

    # f.testInstall()
    # fontName = '%s-%s' % (f.info.familyName, f.info.styleName)

    # fontsize = 18
    # lineheight = 1.1* fontsize
    # spacingstrings = list(stringgenerator())

    # if fontName in installedFonts():
    #         font(fontName)
    # else:
    #     print('font %s not installed' % fontName)
        
    # x = y = margin
    # w = width() - margin*2
    # h = height() - margin*2

    # # set text sample
    # fontSize(fontSize)
    # lineHeight(lineHeight)
    # textBox(spacingstrings, (x, y, w, h))

    ## SECTION 3: OPENTYPE & CASE FEATURES ##

    ## SECTION 4: LANGUAGE SUPPORT ##

    ## SECTION 5: MATH, CURRENCY, NUMS, PUNCTUATION, ETC. ##
