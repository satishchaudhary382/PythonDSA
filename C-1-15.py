# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


sequence_true = [2, 3, 4, 5]
def distinct_num(array):
	if len(set(sequence_true)) == len(array):
		return True
	else:
		return False
print(distinct_num(sequence_true))
