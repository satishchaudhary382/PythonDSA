# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
	if (k & 1) == 0:
		return True
	else:
		return False

even = is_even(9)
print(even)
