import datetime

now = datetime.datetime.now()
newFileName = "xheight_overshoot_check" + now.strftime("%Y_%m_%d-%H_%M_%S")

fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]

textsample = "urus taters thieves smeeth vases garottes aisha smartass busier brags bohea outer hate humuses fee sestetts frag sarges sae hoggs theists toea bee tit fiefs moria barabbas rhombus ras reversi bombs rhus ruffes highth tither messages aromas hobo musette ethos festive sabs maire mouse tavah grasser sargus amir evie sufism evovae semite vivaria rotters barra aerobe garb biremes burst rattier hoofer suavest tose boito toshes emeritus fughetta teemer simitar teff masorah behight bitte fibster titbits tomb iambists suber obviate bream harims teer fasters thars batts erose biotite isis shmooses semmit girt astomous thereof gaus grousers vee baht grosers urger suffers vasts shamers timist tamises sterve gorgeous brooses forums favour tutus traverse summa marriage vor tarries ruts asa them etherise mores thetis arbiters offeror remit gumshoe stot babi brassart stems aerobomb armet agoutas three ravager barterer basest mustees boffs begift merosome gushes trireme grogram behoof bigfeet tate ties bargees misuser heaths shastra ort burgoos offerers faitor goor moms toots guru boffo automats risers measures true grout misaim trema artists gooiest murther father fehm iotas sororise variate gossamer stime bass souses revues breves humous samoa gath forfairs shavers vug mig rathe rubefies mithraea maist boohoos beaths abioses sambas oarage brut tabret arroba"

margin = 50
steps = 7
sizeincrements = 72 / steps
pages = 10
pLength = 200

textsample = textsample.split(" ")

# This function generates formatted strings by randomly picking from the two fonts list, using the size specified, and paragraph length specified.

def textGenerator(fPick, fSize, pLength):
    text = FormattedString()
    for x in range(0, pLength, 1):    
        text.fontVariations(opsz = fSize , wght = 100*y )
        text.append(choice(textsample) + " ", font = choice(fPick[0:2]), fontSize = fSize, fill = 0)
    return text
    

for y in range(0,pages,1):
    # textsamplenew = ""
    # for x in range(0,100,1):
    #     textsamplenew += choice(textsample) + " "
    newPage("LetterLandscape")
    pageHeight = height()-(margin*2)
    boxMargin = (margin/2)
    boxWidth = (width()/2)- boxMargin
    leftBoxHeight = pageHeight - boxMargin
    rightBoxHeight = (pageHeight/2 - boxMargin)
    
    # Box 1
    opticalsize = 72
    textBox(textGenerator(fnames, opticalsize, 200), (margin, margin, boxWidth-boxMargin, leftBoxHeight))
    
    # Box 2
    opticalsize = 36
    textBox(textGenerator(fnames, opticalsize, 200), ((boxMargin*2) + boxWidth, margin+rightBoxHeight+boxMargin, boxWidth-margin, rightBoxHeight))
    
    # Box 3
    opticalsize = 7
    textBox(textGenerator(fnames, opticalsize, 200), ((boxMargin*2) + boxWidth, margin, boxWidth-margin, rightBoxHeight))