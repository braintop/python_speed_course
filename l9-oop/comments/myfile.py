from classes import * 

# Creating instances of the Student class
student1 = Student("Alice", 15, 9)
student2 = Student("Bob", 16, 10)

# Displaying information and promoting students
student1.display_info()
student1.promote()

student2.display_info()
student2.promote()

print("After promotion:")
student1.display_info()
student2.display_info()


# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

# Accelerating and braking
car1.accelerate(30)
car2.accelerate(20)
car1.brake(10)
car2.brake(5)

# Displaying speed
print(f"Car 1 speed: {car1.get_speed()} mph")
print(f"Car 2 speed: {car2.get_speed()} mph")


