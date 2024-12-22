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
		if difference > lst_currency[8]:
			sets[lst_currency[8]] = difference // lst_currency[8]
			difference -= (difference // lst_currency[8])*lst_currency[8]
		for i in range(8,0,-1):
			if difference < lst_currency[i] and difference >= lst_currency[i-1]:
				sets[lst_currency[i-1]] = difference // lst_currency[i-1]
				difference -= difference // lst_currency[i-1] * lst_currency[i-1]
		print(sets)
	
# make_change(10045,20000)
import time
start = time.time()
make_change(12345, 23456)
end = time.time()
print("time in secs: ", end - start)