"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""

test_seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]



for i in test_seq:
	if test_seq.count(i) % 2 != 0:
			print(i)
			break


"""count = seq.count(5)"""



"""
>>> lst = ['A','B','C']
>>> {k: v for v, k in enumerate(lst)}
{'A': 0, 'C': 2, 'B': 1}
"""