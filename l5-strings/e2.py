# In these examples:
# Slicing is done using the syntax [start:end], where start is the index of the first character you want to include, and end is the index after the last character you want to include.
# Omitting start means the slice starts from the beginning of the string.
# Omitting end means the slice goes until the end of the string.
# Negative indices count from the end of the string.
# A step value can be added as a third parameter to slice with a certain interval.
# Reversing a string can be achieved by using a negative step value.
# Remember that Python uses 0-based indexing, so the first character is at index 0, the second at index 1, and so on.

text = "Python Programming"

# Slicing from index 0 to index 5 (excluding index 5)
substring1 = text[0:5]
print(substring1)  # Output: "Python"

# Slicing from index 7 to the end of the string
substring2 = text[7:]
print(substring2)  # Output: "Programming"

# Slicing from index 7 to index 15 (excluding index 15)
substring3 = text[7:15]
print(substring3)  # Output: "Programm"

# Slicing with negative indices (counting from the end of the string)
substring4 = text[-11:-1]
print(substring4)  # Output: "Programmin"

# Slicing with a step (every second character)
substring5 = text[0::2]
print(substring5)  # Output: "Pto rgamn"

# Reversing a string using slicing
reversed_text = text[::-1]
print(reversed_text)  # Output: "gnimmargorP nohtyP"
