class Student:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age

    # Property for name
    @property
    def name(self):
        return self._name

    # Property for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive value")

    # Method to introduce the student
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    # Magic method for string representation
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

# Creating an instance of the Student class
student1 = Student("Alice", 20)

# Using properties and methods
print(student1.name)  # Using the name property
student1.age = 22    # Using the age setter
print(student1.introduce())  # Using the introduce method

# Printing the student object using the __str__ magic method
print(student1)
