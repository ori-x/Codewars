"""
Your task is to make a function that can take any non-negative integer as a argument 
and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

# 1. Convert num to str:
#        str(num)
# 2. Reverse-sort:
#        sorted(list, reverse=True)
# 3. Convert str back to int:
#        int()