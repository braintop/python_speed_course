import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Basic operations
c = a + b  # Element-wise addition
d = a * b  # Element-wise multiplication

print("Array a:", a)
print("Array b:", b)
print("Array c (a + b):", c)
print("Array d (a * b):", d)

# Array manipulation
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:")
print(matrix)

# Transposing the matrix
transposed = matrix.T
print("Transposed matrix:")
print(transposed)

# Array statistics
mean_value = np.mean(a)
max_value = np.max(b)
min_index = np.argmin(c)

print("Mean of array a:", mean_value)
print("Maximum value of array b:", max_value)
print("Index of minimum value in array c:", min_index)
