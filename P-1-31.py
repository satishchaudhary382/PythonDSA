# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

lst_currency = [1,2,5,10,20,50,100,500,1000]

def make_change(amt_charged: float, amt_given:float) -> None:
	assert amt_charged <= amt_given, 'Please give the appropriate amount'
	difference = amt_given - amt_charged
	print(difference)
	sets = dict()
	while difference > 0:
		if difference > 1000:
			thousand_deno = difference // 1000
			difference = difference - thousand_deno * 1000
			sets[1000] = thousand_deno
		if difference < 1000 and difference >= 500:
			five_hundred_deno = difference // 500
			difference = difference - five_hundred_deno * 500
			sets[500] = five_hundred_deno
		if difference < 500 and difference >= 100:
			one_hundred_deno = difference // 100
			difference = difference - one_hundred_deno * 100
			sets[100] = one_hundred_deno
		if difference < 100 and difference >= 50:
			fifty_deno = difference // 50 
			difference -= fifty_deno * 50
			sets[50] = fifty_deno
		if difference < 50 and difference >= 20:
			twenty_deno = difference // 20 
			difference -= twenty_deno * 20
			sets[20] = twenty_deno
		if difference < 20 and difference >=10:
			ten_deno = difference // 10 
			difference -= ten_deno * 10
			sets[10] = ten_deno
		if difference < 10 and difference >= 5:
			five_deno = difference // 5
			difference -= five_deno *5
			sets[5] = five_deno
		if difference < 5 and difference >= 2:
			two_deno = difference // 2
			difference -= two_deno *2
			sets[2] = two_deno
		if difference < 5 and difference >= 1:
			one_deno = difference //1
			difference -= one_deno * 1
			sets[1] = one_deno
	print(sets)

import time
start = time.time()
make_change(22393244,55211232)
end = time.time()
print("time in secs: ", end - start)
# print((5500-2000)//1000)