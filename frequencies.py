"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    newList =[]
    
    for key in items:
            newList.append(str(key))
    
    for i in newList:
        v = newList.count(i)
        frequencies[i] = v
    
    return frequencies

    
    for key in items:
        if not isinstance(key,str):
            items.remove(key)
            items.append(str(key))
    
    for i in items:
        v = items.count(i)
        frequencies[i] = v
    
    return frequencies

