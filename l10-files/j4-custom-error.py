# ========raise
# In Python, the raise statement is used to manually raise
# an exception. It allows you to generate and trigger
# exceptions in your code under specific conditions 
# that you define. This can be particularly useful when
# you want to handle specific error cases or enforce
# certain conditions.
# The basic syntax of the raise statement is as follows:


# Define a custom exception class
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    # Attempt to get the user's age from input
    age = int(input("Enter your age: "))
    
    # Check if the age is negative and raise the custom exception if so
    if age < 0:
        raise MyCustomError("Age cannot be negative.")
    
    # If age is not negative, print the age
    print(f"Your age is: {age}")
    
except MyCustomError as e:
    # Handle the custom exception by printing the error message
    print(f"Error: {e}")
    
except ValueError:
    # Handle the case where the input cannot be converted to an integer
    print("Invalid input. Please enter a valid age.")
