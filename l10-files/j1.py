# Writing to a file with default permissions ('w' mode)
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a sample text.')

# Reading from a file with default permissions ('r' mode)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
