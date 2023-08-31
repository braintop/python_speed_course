# Writing to a file with default permissions ('w' mode)
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a sample text.')

# Reading from a file with default permissions ('r' mode)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


# Open the file in write mode ('w')
file = open('example.txt', 'w')

# Writing data to the file
file.write('Hello, world!\n')
file.write('This is a sample text.')

# Close the file
file.close()

# The file is now closed and no longer accessible
