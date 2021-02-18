"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells 
and carries the "instructions" for the development and functioning of living organisms.


In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 

You have function with one side of the DNA (string, except for Haskell); 
you need to get the other complementary side. 

DNA strand is never empty or there is no DNA at all (again, except for Haskell).
"""

def DNA_strand(dna):
    b_side = ""

    for s in dna: 
        if  == "A":
            b_side += "T"
        elif s == "T":
            b_side += "A"
        elif s == "G":
            b_side += "C"
        elif s == "C":
            b_side += "G"
    
    return b_side

# My notes
"""
Long-winded. Using a dictionary as a reference ex: { A : T } and then joining to a new string would be more efficient. 