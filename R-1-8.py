# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, 
# what is the equivalent index j ≥ 0 such that s[j] references the same element?

string = 'Satish'

# Length of the string
n = len(string)

# Loop through negative indices
for i in range(1, n + 1):
    # Calculate the equivalent positive index
    j = n - i
    # Print the character and both indices
    print(f"Character: {string[-i]}, Positive index: {j}, Negative index: {-i}")
