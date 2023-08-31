class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass 

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return f"{animal.name} says: {animal.speak()}"

# Creating instances and demonstrating polymorphism
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal_sound(dog))  # Calls Dog's speak method
print(animal_sound(cat))  # Calls Cat's speak method
