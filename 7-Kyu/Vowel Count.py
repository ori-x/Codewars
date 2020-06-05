def getCount(inputStr):
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]

    for char in inputStr:
        for vowel in vowels:
            if vowel == char:
                num_vowels += 1

    return num_vowels
    
