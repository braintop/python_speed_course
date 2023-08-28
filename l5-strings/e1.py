# Basic string creation
greeting = "Hello, World!"

# String concatenation
name = "Alice"
message = greeting + " My name is " + name
print(message)

# String indexing and slicing
print("First character:", greeting[0])
print("Last character:", greeting[-1])
print("Characters from index 7 to end:", greeting[7:])
print("Substring:", greeting[7:12])

# String length
length = len(greeting)
print("Length of the string:", length)

# String methods
uppercase = greeting.upper()
lowercase = greeting.lower()
capitalized = greeting.capitalize()
replaced = greeting.replace("Hello", "Hi")

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Capitalized:", capitalized)
print("Replaced:", replaced)

# String formatting
age = 25
formatted_string = "I am {} years old.".format(age)
print(formatted_string)

# f-string formatting (Python 3.6+)
formatted_string_f = f"I am {age} years old."
print(formatted_string_f)

# String splitting and joining
sentence = "This is a sentence to split."
words = sentence.split()
joined_sentence = "-".join(words)
print("Words:", words)
print("Joined:", joined_sentence)
