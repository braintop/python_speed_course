class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

# Creating instances and demonstrating polymorphism
dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Calls Dog's speak method
print(animal_sound(cat))  # Calls Cat's speak method
