"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
"""

x = 1634		


while x > 10:
	for i in str(x):
		x = sum(int(i))
	

print(x)

"""
def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n
"""