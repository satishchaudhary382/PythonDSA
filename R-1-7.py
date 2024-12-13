# Give a single command that computes the sum from Exercise R-1.6, 
# relying on Python’s comprehension syntax and the built-in sum function.

def sum_of_odd(n):
	index = 0
	s = []
	while index < n:
		if index % 2 != 0:
			# s += index
			s.append(index)
		index += 1
	print(s, sum(s))
sum_of_odd(6)