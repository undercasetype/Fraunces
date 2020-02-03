# Remove skew from components

f = CurrentFont()

counter = 1

while counter == 1:
    for g in f:
        for component in g.components:
            print(component.transformation)
            if component.transformation[2] != 0:
                component.transformBy((0,0,(-component.transformation[2]),0,0,0))
            print(component.transformation)
            counter -= 1
            if counter == 0:
                break
            else:
                continue