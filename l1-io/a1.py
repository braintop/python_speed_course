# This Python program demonstrates basic input, calculation, and output operations.

# Print a simple greeting to the console
print("Hello world")
# Read an integer input from the user and store it in the variable num1
num1 = int(input("Enter the first number: "))

# Read another integer input from the user and store it in the variable num2
num2 = int(input("Enter the second number: "))

# Calculate the sum of the two input numbers
sum1 = num1 + num2 

# Print the result along with an explanatory message
print("You have now recorded two numbers whose sum is:", sum1)

# Using an f-string to format the output message with the calculated sum
print(f"You have now recorded two numbers whose sum is: {sum1}")

# Creating a message by concatenating strings and then printing it
message = "You have now recorded two numbers whose sum is: " + str(sum1)
print(message)

# Using string formatting with the `.format()` method to insert the sum into the message
message = "You have now recorded two numbers whose sum is: {}".format(sum1)
print(message)
