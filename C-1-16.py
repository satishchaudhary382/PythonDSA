# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].


print([(i*(enm+1)) for i,enm in enumerate(range(10))])
print([chr(i) for i in range(97,123)])