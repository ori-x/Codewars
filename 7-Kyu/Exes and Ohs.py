"""
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. 
The string can contain any char.
"""

def xo(s):
    x_count = 0
    o_count = 0
    
    for c in s.lower():
        if c == "x":
            x_count += 1 
        elif c == "o":
            o_count += 1
    
    return x_count == o_count

 # My notes
 """
 Let's imagine for a moment I'm new to Python, and I had no idea that the count function for strings existed.... 
 Or, for example, I like to make things difficult for myself. 




 ..... or I forgot. 
 
 return s.count('x') == s.count('o')
 """