from fontTools.designspaceLib import DesignSpaceDocument

"""
Fix designspace axis mapping
2019_11_28 Benedikt Bramboeck, Alphabet
"""

doc = DesignSpaceDocument()

doc_path = '/path/to/designspace_file.designspace'
doc.read(doc_path)

for axis in doc.axes:
    if len(axis.map) is not 0:
        # convert old map to a flat list
        old_map = [item for t in axis.map for item in t] 
        new_map = []
        
        # get extremes of old map
        old_min = min(old_map)
        old_max = max(old_map)
        
        # set new extremes according to min/max of axis
        new_min = axis.minimum
        new_max = axis.maximum

        #calculate new map values
        for value in old_map:
            new_value = (((value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min
            new_map.append(round(new_value))

        #pack flat list back into tuple pair list
        new_map = list(zip(*[iter(new_map)]*2))
    
        axis.map = new_map
doc.write(doc_path)
