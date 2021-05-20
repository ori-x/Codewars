def in_array(array1, array2):
    x = 0
    a3 = []
    
    while x < len(array2):
        for i in array1:
            if i in array2[x] and i not in a3:
                a3.append(i)
        x += 1
    
    return sorted(a3)

