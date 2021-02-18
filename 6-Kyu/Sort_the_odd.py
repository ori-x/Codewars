"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
"""

s_array = [5,3,2,8,1,4]

odds = []
result = []

for num in s_array:
	if num % 2:
		odds.append(num)
		result.append("x")
	else:
		result.append(num)

odds.sort()
usedx = 0

for i, j in enumerate(result):
    if j == "x":
        result[i] = odds[usedx]
        usedx += 1

print(result)


# My notes

"""
Writing pseudo-code definitely helped in visualising this one. After that the first half fell into place. Pulled some hairs
out on trying to find a simple way to replace the 'x's with the new sorted odds. 

1. Create a new list. 
2. Use a for loop to loop through all elements in original list. 
3. Find all odds in the list using the modulus operator.
4. a) Append the odds to seperate 'odds' list. 
   b) Append elements from original array to new list, replacing odds with an "x"

5. Sort odds 

6. Replace "x"s with sorted odds (enumerating is probably not the simplest way to do it)

"""





