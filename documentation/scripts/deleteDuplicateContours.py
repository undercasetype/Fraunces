f = CurrentFont()

for glyph in f:
    
    # Define a list of components for comparison.    
    contourlist = []
    for glyph.contour in glyph:
        contourlist.append(glyph.contour.bounds)
    
    for contour in contourlist:
        # Start a counter at -1, to factor in that there should always be atleast 1 contour that is the same across sets.
        duplicate_contours = -1
        
        # Iterates through contours and increases duplicate_contours count whenever it finds a shape with the same bounds.
        for glyph.contour in glyph:
            if glyph.contour.bounds == contour:
                duplicate_contours += 1
                
        # While loop stops deleting contours once the duplicate_contours counter hits zero. If it finds a shape that is the same
        # bounds, the for loop breaks, and the counter subtracts 1.
        while duplicate_contours > 0:
            for glyph.contour in glyph:
                if glyph.contour.bounds == contour:
                    glyph.removeContour(glyph.contour)
                    break
                else:
                    continue
            duplicate_contours -= 1
