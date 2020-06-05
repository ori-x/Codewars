def first_non_consecutive(array):
    prev = array[0]
    for num in array[1:]:
        if (prev + 1) != num:
            return num
            break
        prev += 1
