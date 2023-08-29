# Explanation: Dictionaries can be nested, allowing
# for more complex data structures. In this example,
#  the employee dictionary contains a nested department
# dictionary.

# These examples demonstrate the usage of dictionaries
# in Python, with explanations tailored for Java experts
# who have experience in web development. 
# They cover creating and accessing dictionaries,
# using dictionary methods, iterating through dictionaries,
# dictionary comprehension, and working with nested dictionaries.






# Creating a nested dictionary
employee = {
    "name": "Alice",
    "department": {
        "name": "Engineering",
        "location": "Building A"
    }
}

# Accessing nested dictionary values
print("Employee:", employee["name"])
print("Department:", employee["department"]["name"])
print("Location:", employee["department"]["location"])
