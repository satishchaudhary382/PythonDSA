# Give a single command that computes the sum from Exercise R-1.4, 
# relying on Python’s comprehension syntax and the built-in sum function.

sample_array = [9,8,7,6,5,3,2,1,100,45,23,46,22,76]
def sum_of_squares(array):
	return sum([i*i for i in array])

print(sum_of_squares(sample_array))
