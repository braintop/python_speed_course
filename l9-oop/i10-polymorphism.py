class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating an array of Animal objects
animals = [Dog(), Cat(), Dog(), Cat()]

# Downcasting to Dog and Cat and calling their specific methods
for animal in animals:
    if isinstance(animal, Dog):# if(animal instanceof Dog){}
        print("Dog says:", animal.speak())
    elif isinstance(animal, Cat):
        print("Cat says:", animal.speak())
    else:
        print("Unknown animal says:", animal.speak())
