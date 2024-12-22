# Write a short Python function that counts the number of vowels in a given
# character string.

def count_vowels(string:str) -> int:
    char = [i for i in string]
    count = 0
    for vowel in char:
        if vowel in ['a','e','i','o','u']:
            count += 1
            print(vowel, count)
    print("Total vowel in string is ", count)

count_vowels("Satish")
