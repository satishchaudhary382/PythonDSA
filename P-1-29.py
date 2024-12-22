#Write a Python program that outputs all possible strings formed by using
#the characters c , a , t , d , o , and g exactly once.

import itertools

characters = ['c','a','t','d','o','g']
all_strings = list()
for length in range(1,len(characters)):
    lists = [i for i in itertools.permutations(characters,length)]
    for i in lists:
        all_strings.append("".join(i))

print(all_strings)
