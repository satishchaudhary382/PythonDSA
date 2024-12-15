# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

sequence_false = [2, 4, 6, 8]
sequence_true = [2, 3, 4, 5]

def product_odd(array):
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i]*array[j] % 2 != 0 and (i != j or j!= i):
				print((array[i],array[j]),True)
				return 
	print(False)

product_odd(sequence_false)