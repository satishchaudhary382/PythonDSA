# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_of_odd(n):
	index = 0
	s = 0
	while index < n:
		if index % 2 != 0:
			s += index
		index += 1
	print(s)
sum_of_odd(6)