from abc import ABC, abstractmethod

# Abstract class in Python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete classes inheriting from abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Using the concrete classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
