class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount

    def get_speed(self):
        return self.speed

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def promote(self):
        self.grade += 1

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

def main(): # you can replace main with any name 
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Civic", 2023)


if __name__ == "__main__": # line 35 is the main 
    main()

# if we run this script - main 
# if this script import from other script - !main     

