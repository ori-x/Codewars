"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 

Implement a function that determines whether a string that contains only letters is an isogram. 
    Assume the empty string is an isogram. 
    Ignore letter case.

 """

def is_isogram(str1):
    str1 = str1.upper()
    isogram = ""

    for char in str1:
        if char not in isogram:
            isogram += char

    return str1 == isogram

# Very roundabout way of doing it. My brain took a detour on this one. 
# A logical solution would be to compare string lengths. 


