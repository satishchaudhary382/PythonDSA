# Python’s random module includes a function shuﬄe(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuﬄe function.

import random
import time
start = time.time()
sequence_true = [2, 3, 4, 5,323,121,4541,313]
random.shuﬄe(sequence_true)
print(sequence_true)
end = time.time()
perf_inbuilt = end - start
print("Inbuilt library random ", perf_inbuilt)

def random_shuffle(array):
	minimum = min(array)
	maximum = max(array)
	random_array = []
	for _ in range(len(array)):
		rand_num = random.randint(minimum, maximum)
		if random_array is None:
			random_array.append(rand_num)
		else:
			while len(random_array) < len(array):
				if rand_num is not random_array:
					random_array.append(rand_num)

custom_start = time.time()
random_shuffle(sequence_true)
custom_end = time.time()
custom_inbuilt = custom_end - custom_start
print("Performance of custom random shuffle ", custom_inbuilt)
if custom_inbuilt < perf_inbuilt:
	print('Good')
