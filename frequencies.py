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