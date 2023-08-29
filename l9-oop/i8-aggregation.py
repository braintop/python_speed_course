class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start(self):
        print("Car is starting")
        self.engine.start()

class Driver:
    def __init__(self, name):
        self.name = name

    def drive_car(self, car):
        print(f"{self.name} is driving the car")
        car.start()

# Creating objects using composition
my_car = Car()
alice = Driver("Alice")
alice.drive_car(my_car)
