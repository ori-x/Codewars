"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""

def square_digits(num):

    squares = ""

    for digit in str(num):
        digit = int(digit)**2
        squares += str(digit)

    return int(squares)

# My notes
"""
   In hindsight, the for loop could have easily have been reduced to one line like so:

     squares += str(int(digit)**2)

  It's finally starting to hit me: simple substitution from maths class can go a long way in making a Python script easier to read. 
  Does this over-simplifcation begin to complicate things for others reading the code...?

     return int(''.join(str(int(digit)**2) for digit in str(num)))
"""
