# Define a function to calculate the square of a number
def square(x):
    return x ** 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map to calculate squares of numbers
squared_numbers = map(square, numbers)

# Iterate over the iterator using a loop
for squared_value in squared_numbers:
    print(squared_value)
