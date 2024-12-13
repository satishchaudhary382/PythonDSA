# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

sample_array = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]
def sum_of_positive(array: int) -> int:
	s = 0
	for i in sample_array:
		if i > 0:
			s += i
	return s
print(sum_of_positive(sample_array))
