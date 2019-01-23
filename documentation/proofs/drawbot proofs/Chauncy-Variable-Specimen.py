# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     ShowFontContent.py
#
#     Print the values of the specified font for naming, info and features
#     and generate a simple 1000 x 1000 PDF, showing part of the glyph set.
#     This is the simple demo version of the FontSpecimen.py that will generate 
#     a full specimen of the font.
#
import pagebot
from pagebot import getContext
from pagebot.fonttoolbox.fontpaths import getTestFontsPath
from pagebot.fonttoolbox.objects.font import findFont, Font
from pagebot.document import Document
from pagebot.style import *
from pagebot.elements import * # Import all types of page-child elements for convenience
from pagebot.toolbox.color import color
from pagebot.toolbox.units import em, p, pt, mm, inch, px
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.constants import *
from pagebot.fonttoolbox.variablefontbuilder import getVarFontInstance

c = getContext()
EXPORT_PATH = '_export/FontContent.pdf'

#Load Font
DEFAULT_FONT_PATH = 'fonts/'
FONT_PATH = DEFAULT_FONT_PATH + 'ChauncyRegular-VF.ttf'
FONT_PATH2= DEFAULT_FONT_PATH + 'ChauncyItalic-VF.ttf'

# Function to know if the fonts is loading
f = Font(FONT_PATH)
if f is None:
    print('%s cannot be found' % FONT_PATH)
else:
    print('Done')

f2 = Font(FONT_PATH2)
if f2 is None:
    print('%s cannot be found' % FONT_PATH2)
else:
    print('Done')

#Default Axes Descriptions
axesDescriptions = { 'wght': 'Weight', 'wdth': 'Width', 'opsz': 'Optical size',}

# Get the axis of the font that is loaded
for axisName, (minValue, defaultValue, maxValue) in f.axes.items():
    print(axisName, minValue, defaultValue, maxValue, axesDescriptions.get(axisName, 'unknown axis'))
for axisName, (minValue, defaultValue, maxValue) in f2.axes.items():
    print(axisName, minValue, defaultValue, maxValue, axesDescriptions.get(axisName, 'unknown axis'))

#ROMAN FONTS
MAXOPTICAL = getVarFontInstance(f.path, dict(opsz=72.0))
MINOPTICAL = getVarFontInstance(f.path, dict(opsz=6.0))
H2OPTICAL = getVarFontInstance(f.path, dict(opsz=36.0))
#ITALICFONTS
MAXOPTICALIT = getVarFontInstance(f2.path, dict(opsz=72.0))
MINOPTICALIT = getVarFontInstance(f2.path, dict(opsz=6.0))
H2OPTICALIT = getVarFontInstance(f2.path, dict(opsz=36.0))


#Function to make the docuemnt
def makeDocument():
    #Parameters of the docuemnt
    context = getContext()
    W, H = pt(1920, 1080)
    padheight = pt(70)
    padside = pt(466)
    PADDING = padheight, padside, padheight, padside
    G = mm(4)
    PW = W - 2*padside 
    PH = H - 2*padheight
    CW = (PW - (G*2))/3 
    CH = PH
    GRIDX = ((CW, G), (CW, 0))
    GRIDY = ((CH, 0),)
    fontSizeH1 = 144
    points =' / ' + str(fontSizeH1)

    # Function for the first column in the main page layout
    def firstColumnWaterfall(b, fontStyle):
        s = c.newString('', style=dict(font=f))
        s2 = c.newString('', style=dict(font=f))
        CW2 = (PW - (G*2))/3 # Column width
        for n in range(4):
        	fontSize = pt(12+n*1)
	        leading = pt((12+n*1)+3)
        	if n < 3:
	        	leading2 = pt(((12+n*1)*n)+90+n*4)
	        else:
	        	leading2=((12+n*1)*n)+86+n
       		s += c.newString( b + '\n', style=dict(font=fontStyle, fontSize=fontSize, leading=leading))
        	s2 += c.newString( str(fontSize) + '/' +str(leading) + '\n', style=dict(font=fontStyle, fontSize=10, leading=leading2))
        newTextBox(s ,parent=page, w=CW2, h=pt(700),font=f, pt=pt(160), nextElementName='e2',conditions=[Left2Left(),Top2Top(), Overflow2Next()])
        newTextBox(s2 ,parent=page, w=CW2, h=pt(700),font=f, pt=(pt(70)), nextElementName='e2',conditions=[Left2Left(),Top2Top(), Overflow2Next()])
        doc.solve()
    
    # Function for the second column in the main page layout
    def secondColumnWaterfall(b, fontStyle):
        s = c.newString('', style=dict(font=f))
        s2 = c.newString('', style=dict(font=f))
        CW2 = (PW - (G*2))/3 # Column width
        for n in range(3):
        	fontSize=pt(16+n*2)
        	leading=pt((12+n*2)+6)
        	if n < 1:
        		leading2 = (((12+n*2)+6)*n*2)+90+n*10
        	elif n < 2:
        		leading2 = (((12+n*2)+6)*n*2)+110+n*10
        	else:
        		leading2 = ((((12+n*2)+6)*n*2)+76+n*10)+n*6
        	s += c.newString( b + '\n', style=dict(font=fontStyle, fontSize=fontSize, leading=leading ))
        	s2 += c.newString( str(fontSize) + '/' + str(leading) + '\n', style=dict(font=fontStyle, fontSize=10, leading=leading2 ))
        newTextBox(s ,parent=page, w=CW2, h=pt(700),font=f, pt=pt(160), conditions=[Right2Right(),Top2Top()])
        newTextBox(s2 ,parent=page, w=CW2, h=pt(700),font=f, pt=(pt(70)), conditions=[Right2Right(),Top2Top()])
        doc.solve()

    # Function for the Waterfall layout
    def typeWaterfall(x, fontStyle, PageDescription, pageNumber):
        newTextBox(PageDescription, style=subtitle, w=PW, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        newTextBox(pageNumber, style=subtitle, xTextAlign=RIGHT, w=50, h=PH, parent=page, columnAlignY = TOP, conditions=(Right2Right(), Top2Top()))
        st = c.newString('', style=dict(font=f))
        st2 = c.newString('', style=dict(font=f))
        for n in range(7):
            if n < 4:
                fontSize=144-n*24
                leading=(144-n*24)+24
                leading2=(144-n*24)+24
            else:
                fontSize=108-n*12
                leading=None
                leading2=(108-n*12)+24
            st += c.newString( x + '\n', style=dict(font=fontStyle, fontSize=fontSize, leading=leading))
            st2 += c.newString( str(fontSize) + 'pt' + '\n', style=dict(font=fontStyle, fontSize=12, leading=leading2))
        newTextBox(st ,parent=page, padding=pt(4), x=pt(60), y= pt(950), w=W, font=f,
                    cconditions=[Left2Left(), Top2Top(),  Overflow2Next()],
                    yAlign=TOP, xAlign=LEFT,)
        newTextBox(st2 ,parent=page, padding=pt(4), x=pt(60), y= pt(940), w=W, font=f,
                    cconditions=[Left2Left(), Top2Top(),  Overflow2Next()],
                    yAlign=TOP, xAlign=LEFT,)
        return doc 
        doc.solve()

     # Function for the Waterfall layout
    def typeWaterfallTwolines(x, fontStyle, PageDescription, pageNumber):
        newTextBox(PageDescription, style=subtitle, w=PW, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        newTextBox(pageNumber, style=subtitle, xTextAlign=RIGHT, w=50, h=PH, parent=page, columnAlignY = TOP, conditions=(Right2Right(), Top2Top()))
        st = c.newString('', style=dict(font=f))
        st2 = c.newString('', style=dict(font=f))
        for n in range(7):
            if n < 4:
                fontSize=144-n*24
                leading=(144-n*24)+24
                leading2=(144-n*24)+24
            else:
                fontSize=108-n*12
                leading=None
                leading2=(108-n*12)+24
            st += c.newString( x + '\n', style=dict(font=fontStyle, hyphenation=False, fontSize=fontSize, leading=leading))
            st2 += c.newString( str(fontSize) + 'pt' + '\n', style=dict(font=fontStyle, fontSize=12, leading=leading2))
        newTextBox(st ,parent=page, hyphenation=False, padding=pt(4), x=pt(60), y= pt(950), w=W-50, font=f,
                    cconditions=[Left2Left(), Top2Top(),  Overflow2Next()],
                    yAlign=TOP, xAlign=LEFT,)
        newTextBox(st2 ,parent=page, padding=pt(4), x=pt(60), y= pt(780), w=W, font=f,
                    cconditions=[Left2Left(), Top2Top(),  Overflow2Next()],
                    yAlign=TOP, xAlign=LEFT,)
        return doc 
        doc.solve()


    # Create a new document with 1 page. Set overall size and padding.
    doc = Document(w=W, h=H, padding=PADDING, gridX=GRIDX, gridY=GRIDY, context=context)
    view = doc.view
    page = doc[1]

    subtitle = dict(font=f, fontSize=pt(18), leading=pt(28))
    pagePaddings = (50, 50, 50, 50)

    # Page1
    # Function to make the main page layout 
    def mainPage(fontStyle1, fontStyle2, pageNumber, defaultfont):
        # New text box for the Title
        maintitle = context.newString("Amstelvar", style=dict(font=fontStyle1, xTextAlign=CENTER, fontSize=pt(96), leading=pt(115)))
        newTextBox(maintitle, w=PW, h=PH, parent=page, columnAlignY = TOP, xTextAlign=CENTER, conditions=(Center2Center(), Top2Top()))
        subtitle = dict(font=fontStyle2, fontSize=pt(18), leading=pt(28))
        subtitle2 = dict(font=defaultfont, fontSize=pt(18), leading=pt(28))
        newTextBox(pageNumber, w=W-100, pt=-20, h=PH+100, parent=page, xAlign=RIGHT, xTextAlign=RIGHT, style=subtitle2, conditions=(Center2Center(), Top2Top()))
        newTextBox("Series by David Berlow", style=subtitle, pt = pt(100), w=PW, h=PH, parent=page, columnAlignY = BOTTOM, xTextAlign=CENTER, conditions=(Center2Center(), Bottom2Bottom()))
        # 3 columns
        heightCol = pt(700)
        textString = "ABCDEFG HIJKLMN OPQRSTU VWXYZ&! abcdefghij klmnopqrs tuvwxyzĸ¢ 1234567890"
        centertext = context.newString(textString, style=dict(font=fontStyle1, xTextAlign=CENTER, fontSize=pt(60), leading=pt(69)))
        CW2 = (PW - (G*2)) # Column width
        style3 = dict(font=f, fontSize=pt(60), leading=pt(69), hyphenation=None, prefix= None, postfix=None)
        newTextBox(centertext, style=style3, w=CW, h=heightCol, pt = pt(158), xTextAlign=CENTER, parent=page, conditions=[Center2Center(), Top2Top()])
        text4 = "Betreed de wereld van de invloedrijke familie Plantin en Moretus. Christophe Plantin bracht zijn leven door in boeken. Samen met zijn vrouw en vijf dochters woonde hij in een imposant pand aan de Vrijdagmarkt. Plantin en Jan Moretus hebben een indrukwekkende drukkerij opgebouwd. Tegenwoordig is dit het enige museum ter wereld dat ..."
        style4 = dict(font=fontStyle2, fontSize=pt(28), leading=pt(34))
        newTextBox(text4, style=style4, xTextAlign=JUSTIFIED, w=CW2+26, h=pt(380), parent=page, pt=pt(174), conditions=[Right2Right(), Bottom2Bottom()])
        style5 = dict(font=defaultfont, fontSize=pt(10))
        b = ("Hyni në botën e familjes me ndikim Plantin dhe Moretus. Christophe Plantin e kaloi jetën mes librave. Së bashku me gruan dhe pesë bijat e tij, ai jetonte në një pronë imponuese në Vrijdagmarkt. Plantin dhe Jan Moretus krijuan një biznes shtypës mbresëlënës. Sot, ky është muze i vetëm në botë që mbresëlënës do gruan ... \n ")
        c = ("Hyni në botën e familjes me ndikim Plantin dhe Moretus. Christophe Plantin e kaloi jetën mes librave. Së bashku me gruan dhe pesë bijat e tij, ai jetonte në një pronë imponuese në Vrijdagmarkt. Plantin dhe Jan Moretus krijuan një biznes shtypës mbresëlënës. Sot, ky është muze i vetëm në botë që mbresëlënës do ... \n ")
        newTextBox('60pt/72pt' ,fontSize=pt(10), parent=page, w=CW-60, h=heightCol,font=f, pt=pt(146),conditions=[Center2Center(),Top2Top()])
        newTextBox('28pt/34pt' ,fontSize=pt(10), parent=page, w=CW2, h=pt(380),font=f, pt=pt(160),conditions=[Left2Left(),Bottom2Bottom()])
        firstColumnWaterfall(b, fontStyle2)
        secondColumnWaterfall(c, fontStyle2)
        doc.solve()

    # Parameters of the function
    fontStyle1 = H2OPTICAL.path
    fontStyle2 = f.path
    defaultfont = f.path
    pageNumber = '1'
    mainPage(fontStyle1, fontStyle2, pageNumber, defaultfont)


    # Page2
    # Function to make the one column layout
    page = page.next
    def oneColumnPage(fontStyle, textString, PageDescription, pageNumber):
        astring = context.newString(textString, style=dict(font=fontStyle, xTextAlign=CENTER, fontSize=fontSizeH1, leading=pt(163)))
        page.padding = pagePaddings
        padd= pt(100)
        PW2 = W - 2*padd
        newTextBox(astring, pt= pt(130), w=PW2, h=H, hyphenation=False, parent=page, conditions=(Center2Center(), Middle2Middle()))
        newTextBox(PageDescription, style=subtitle, w=PW, hyphenation=False, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        newTextBox(pageNumber, style=subtitle, xTextAlign=RIGHT, w=50, h=PH, parent=page, columnAlignY = TOP, conditions=(Right2Right(), Top2Top()))
        #newTextBox('144pt', style=subtitle, xTextAlign=CENTER, w=200, h=50, parent=page, columnAlignY = TOP, conditions=(Center2Center(), Top2Top()))
        doc.solve()
    
    # Parameters of the function
    textString = "Aa Bb Cc Dd Ee Ff \nGg Hh Ii Jj Kk \nLl Mm Nn Oo Pp \nQq Rr Ss Tt Uu \nVv Ww Xx Yy Zz"
    PageDescription = "Opsz-max camelcase roman" + points
    fontStyle = MAXOPTICAL.path
    pageNumber = '2'
    oneColumnPage(fontStyle, textString, PageDescription, pageNumber)

    # Page3
    page = page.next
    PageDescription = "Opsz-default camelcase roman" + points
    fontStyle = f.path
    pageNumber = '3'
    oneColumnPage(fontStyle, textString, PageDescription, pageNumber)

    #Page4
    page = page.next
    PageDescription = "Opsz-min camelcase roman" + points
    fontStyle = MINOPTICAL.path
    pageNumber = '4'
    oneColumnPage(fontStyle, textString, PageDescription, pageNumber)

    # Page 5
    #Function to make the 3 column layout
    page = page.next 
    def threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription, pageNumber):
        page.padding = pagePaddings
        CW3 = (W-120)/3 # Column width
        cstring = context.newString(textString, style=dict(font=fontStyle1, xTextAlign=CENTER, fontSize=fontSizeH1, leading=pt(163)))
        dstring = context.newString(textString, style=dict(font=fontStyle2, xTextAlign=CENTER, fontSize=fontSizeH1, leading=pt(163), hyphenation=None))
        spreads= dict(font=fontStyle3, fontSize=fontSizeH1, leading=pt(163))
        newTextBox(cstring, w=(CW3+10), parent=page, conditions=[Left2Left(), Middle2Middle()])
        newTextBox(textString, style=spreads, w=CW3, xTextAlign=CENTER, parent=page, conditions=[Center2Center(), Middle2Middle()])
        newTextBox(dstring, w=CW3, parent=page, conditions=[Right2Right(), Middle2Middle()])
        newTextBox(PageDescription, style=subtitle, w=PW, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        newTextBox(pageNumber, style=subtitle, xTextAlign=RIGHT, w=50, h=PH, parent=page, columnAlignY = TOP, conditions=(Right2Right(), Top2Top()))
        #newTextBox('144pt', style=subtitle, xTextAlign=CENTER, w=200, h=50, parent=page, columnAlignY = TOP, conditions=(Center2Center(), Top2Top()))

        doc.solve()

    # Parameters of the function
    textString = "ABCDE\nFGHIJK\nLMNOP\nQRSTU\nVWXYZ"
    PageDescription = "Opsz-min opsz-default opsz-max uppercase roman" + points
    fontStyle1 = MINOPTICAL.path
    fontStyle2 = MAXOPTICAL.path
    fontStyle3 = f.path
    pageNumber = '5'
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription, pageNumber)

    # Page 6
    page = page.next 
    textString = 'adhesion'
    PageDescription = "Opsz-min opsz-default opsz-max lowercase roman" + points
    fontStyle1 = MINOPTICAL.path
    fontStyle2 = MAXOPTICAL.path
    fontStyle3 = f.path
    pageNumber = '6'
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription, pageNumber)

    # Page 7
    page = page.next
    page.padding = pagePaddings
    x = 'ADHESION'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall uppercase roman'
    pageNumber = '7'
    typeWaterfallTwolines(x, fontStyle, PageDescription, pageNumber)

    # Page 8
    page = page.next
    page.padding = pagePaddings
    x = 'adhesion'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall lowercase roman'
    pageNumber = '8'
    typeWaterfall(x, fontStyle, PageDescription, pageNumber)

    # Page 9
    page = page.next
    page.padding = pagePaddings
    x = '1234567890‘?“!(%)[#]{@}/&\$:;,._^*'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall numerals and punctuation roman'
    pageNumber = '9'
    typeWaterfallTwolines(x, fontStyle, PageDescription, pageNumber)
    
    # Page 10
    page = page.next
    page.padding = pagePaddings
    x = '₡$€£₣₤₦₩₫₭₱₲₵₹₺₼₽'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall monetary'
    pageNumber = '10'
    typeWaterfall(x, fontStyle, PageDescription, pageNumber)
    
    # Page 1 Italic
    page = page.next
    fontStyle1 = H2OPTICALIT.path
    fontStyle2 = f2.path
    defaultfont = f.path
    pageNumber = '11'
    mainPage(fontStyle1, fontStyle2, pageNumber, defaultfont)

    # Page 2 Italic
    page = page.next
    textString = "Aa Bb Cc Dd Ee Ff \nGg Hh Ii Jj Kk \nLl Mm Nn Oo Pp \nQq Rr Ss Tt Uu \nVv Ww Xx Yy Zz"
    PageDescription = "Opsz-max camelcase italic" + points
    fontStyle = MAXOPTICALIT.path
    pageNumber = '12'
    oneColumnPage(fontStyle, textString, PageDescription, pageNumber)

    # Page 3 Italic
    page = page.next
    PageDescription = "Opsz-default camelcase italic" + points
    fontStyle = f2.path
    pageNumber = '13'
    oneColumnPage(fontStyle, textString, PageDescription, pageNumber)

    # Page 4 Italic
    page = page.next
    PageDescription = "Opsz-min camelcase italic" + points
    fontStyle = MINOPTICALIT.path
    pageNumber = '14'
    oneColumnPage(fontStyle, textString, PageDescription, pageNumber)

    # Page 5 Italic
    page = page.next
    textString = "ABCDE\nFGHIJK\nLMNOP\nQRSTU\nVWXYZ"
    PageDescription = "Opsz-min opsz-default opsz-max uppercase italic" + points
    fontStyle1 = MINOPTICALIT.path
    fontStyle2 = MAXOPTICALIT.path
    fontStyle3 = f2.path
    pageNumber = '15'
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription, pageNumber)

    # Page 6 Italic
    page = page.next 
    textString = 'abcde\nfghijk\nlmnop\nqrstu\nvwxyz'
    PageDescription = "Opsz-min opsz-default opsz-max lowercase italic" + points
    fontStyle1 = MINOPTICALIT.path
    fontStyle2 = MAXOPTICALIT.path
    fontStyle3 = f2.path
    pageNumber = '16'
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription, pageNumber)
    doc.solve()

    # Page 7 Italic
    page = page.next
    page.padding = pagePaddings
    x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall uppercase italic'
    pageNumber = '17'
    typeWaterfallTwolines(x, fontStyle, PageDescription, pageNumber)
    doc.solve()

    # Page 8 Italic
    page = page.next
    page.padding = pagePaddings
    x = 'abcdefghijklmnopqrstuvwxyz'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall lowercase italic'
    pageNumber = '18'
    typeWaterfall(x, fontStyle, PageDescription, pageNumber)
    doc.solve()

    # Page 9 Italic
    page = page.next
    page.padding = pagePaddings
    x = '1234567890‘?“!(%)[#]{@}/&\$:;,._^*'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall numerals and punctuation roman'
    pageNumber = '19'
    typeWaterfallTwolines(x, fontStyle, PageDescription, pageNumber)
    doc.solve()

    # Page 10 Italic
    page = page.next
    page.padding = pagePaddings
    x = '₡$€£₣₤₦₩₫₭₱₲₵₹₺₼₽'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall monetary'
    pageNumber = '20'
    typeWaterfall(x, fontStyle, PageDescription, pageNumber)
    
    page.solve()
    return doc

# Export the document to this PDF file.
doc = makeDocument()
doc.export('_export/Amstelvar-Specimen.pdf') 