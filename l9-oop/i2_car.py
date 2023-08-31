class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"This is a {self.make} {self.model}."
        

# Creating instances (objects) of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Using methods to interact with objects
print(car1.get_info())
print(car2.get_info())


