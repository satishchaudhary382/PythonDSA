# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def repeat_divide(number: int) -> int:
	count = 0
	new_number = number
	while new_number > 2:
		value = new_number / 2
		new_number = value
		count += 1
	print(new_number, count)

repeat_divide(1230)
