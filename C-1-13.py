# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.


# pusedo code 
'''
function reverselist(lst):
	i = 0; j = len(array)-1
	for element in lst:
		lst[i] == lst[j]
'''
import time
start = time.time()
sample_array = [i for i in range(1,1000)]
def reverselist(lst):
	i = 0; j = len(lst)-1
	for _ in lst:
		lst[i], lst[j] = lst[j], lst[i]
		if i < j:
			i+=1
			j-=1
		else:
			break
	return lst
end = time.time()
b = reverselist(sample_array)


start_1 = time.time()
a = sample_array[::-1]
end_1 = time.time()
print(end_1 -start_1)
print(end - start)
print((end - start)<(end_1 -start_1))