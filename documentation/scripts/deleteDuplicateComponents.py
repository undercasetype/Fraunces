f = CurrentFont()

for glyph in f:    
    contourlist = []
    for glyph.contour in glyph:
        contourlist.append(glyph.contour.bounds)
    
    for contour in contourlist:
        duplicate_contours = -1
        for glyph.contour in glyph:
            if glyph.contour.bounds == contour:
                duplicate_contours += 1
        while duplicate_contours > 0:
            for glyph.contour in glyph:
                if glyph.contour.bounds == contour:
                    glyph.removeContour(glyph.contour)
                    break
                else:
                    continue
            duplicate_contours -= 1
