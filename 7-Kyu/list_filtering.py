"""
In this kata you will create a function that takes a list of non-negative integers and strings 
and returns a new list with the strings filtered out.
"""

def filter_list(l):
    return [i for i in l if type(i) is int]

# My notes
"""
I imagine swapping out type() for isinstance() would also make sense. 
"""