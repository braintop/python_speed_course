# In Python, a list is a versatile data structure
# that can hold a collection of items. Lists are ordered,
# mutable (meaning you can change their contents), 
# and can contain items of different data types.
# Lists are defined using square brackets []
# and items are separated by commas.
# Here's how you can work with lists:

empty_list = []                     # Create an empty list
numbers = [1, 2, 3, 4, 5]           # Create a list of numbers
fruits = ['apple', 'banana', 'orange']  # Create a list of strings
mixed_list = [1, 'apple', True]      # Create a list with mixed data types

fruits = ['apple', 'banana', 'orange']
print(fruits[0])   # Output: 'apple'
print(fruits[1])   # Output: 'banana'
print(fruits[-1])  # Output: 'orange' (negative indexing starts from the end)

numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]   # Subset: [2, 3, 4]

fruits = ['apple', 'banana', 'orange']
fruits[1] = 'grape'    # Change 'banana' to 'grape'
fruits.append('kiwi')  # Add 'kiwi' to the end
fruits.insert(1, 'pear')  # Insert 'pear' at index 1
fruits.remove('apple')    # Remove 'apple'

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()        # Sort the list in ascending order
numbers.reverse()     # Reverse the list
count_1 = numbers.count(1)  # Count occurrences of 1
numbers.pop()         # Remove and return the last element
