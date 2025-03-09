numbers = [1, 2, 3, 4, 5, 6]
words = ["hello", "world"]

# Square numbers
squares = [x**2 for x in numbers]

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]

# Convert strings to uppercase
uppercase_words = [word.upper() for word in words]

# Create a list of tuples (number, square)
num_square_pairs = [(x, x**2) for x in numbers]

# Print results
print("Squares:", squares)
print("Even numbers:", evens)
print("Uppercase words:", uppercase_words)
print("Number-Square pairs:", num_square_pairs)
