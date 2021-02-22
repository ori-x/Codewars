"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once
"""

def solution(number):
    a = 0
    
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            a += num
        else:
            continue
    
    return(a)