# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.


def is_multiple(n,m):
	if n % m == 0:
		return True
	else:
		return False

a = is_multiple(20,10)
print(a)
