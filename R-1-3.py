# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

sample_array = [9,8,7,6,5,3,2,1,100,45,23,46,22,76]
def minmax(array):
	if not array:
		raise ValueError("Array is empty")
	min_value = array[0]
	max_value = array[0]

	for num in sample_array[1:]:
		if num < min_value:
			min_value = num
		if num > max_value:
			max_value = num

	return min_value, max_value

print(minmax(sample_array))
