def duplicate_encode(word):

    word = list(word.lower())
    word_copy = ""

    for word_char in word:

        number_letter = word.count(word_char)

        if number_letter >= 2:
            word_copy += ")"
        else:
            word_copy += "("

    return word_copy
    
