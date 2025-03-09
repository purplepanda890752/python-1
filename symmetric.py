# Define two sets and find symmetric difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
sym_diff = set1 ^ set2  

# Define a list of numbers and words
numbers = [1, 2, 3, 4, 5, 6]
words = ["hello", "world"]

# List comprehensions
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
uppercase_words = [word.upper() for word in words]
num_square_pairs = [(x, x**2) for x in numbers]

# Print results
print("Symmetric Difference:", sym_diff)
print("Squares:", squares)
print("Even numbers:", evens)
print("Uppercase words:", uppercase_words)
print("Number-Square pairs:", num_square_pairs)
