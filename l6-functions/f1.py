def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}! How are you?")

def add(a, b):
    """This function adds two numbers and returns the result."""
    result = a + b
    return result

def calculate_circle_area(radius):
    """This function calculates the area of a circle given its radius."""
    pi = 3.14159
    area = pi * radius ** 2
    return area


# Calling the greet function
greet("Alice")
greet("Bob")

# Calling the add function
sum_result = add(5, 3)
print("Sum:", sum_result)

# Calling the calculate_circle_area function
radius = 4.5
circle_area = calculate_circle_area(radius)
print("Circle area:", circle_area)
