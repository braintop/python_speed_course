# Creating a dictionary
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Physics"]
}

# Adding a new key-value pair
student["major"] = "Computer Science"

# Removing a key-value pair
del student["age"]

# Checking if a key exists
if "courses" in student:
    print("Student is taking courses:", student["courses"])
