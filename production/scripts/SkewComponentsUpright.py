

"""
Skew all components back to being upright
"""

f = CurrentFont()

for g in f:
    for c in g.components:
        t = list(c.transformation)
        t[2] = 0
        c.transformation = t

print("Done")