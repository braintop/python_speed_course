#new_list = [expression for item in iterable if condition]

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#generator = (expression for item in iterable if condition)

even_generator = (x for x in range(10) if x % 2 == 0)
print(list(even_generator))  # Output: [0, 2, 4, 6, 8]
