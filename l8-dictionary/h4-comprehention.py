# Creating a dictionary using dictionary comprehension
numbers_squared = {num: num ** 2 for num in range(1, 6)}

# Printing the squared values
for num, squared in numbers_squared.items():
    print(f"{num} squared is {squared}")
