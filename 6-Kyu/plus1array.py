def up_array(arr):
    arr.reverse()
    
    if not arr:
        return None
    
    for j in arr:
        if j < 0 or j > 9:
            return None
        
    for i, val in enumerate(arr):
        if val >= 0 and val < 9:
            arr[i] += 1
            break
        elif val == 9:
            arr[i] = 0
        else:
            return None

        
    if len(arr) > 0 and arr[-1] == 0:
        arr.append(1)
    
    arr.reverse()
    
    return(arr)