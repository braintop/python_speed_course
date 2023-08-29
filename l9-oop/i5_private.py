class MyClass:
    def __init__(self):
        self.public_var = "This is public"

obj = MyClass()
print(obj.public_var)  # Accessing public_var

class MyClass2:
    def __init__(self):
        self.__private_var = "This is private"

obj = MyClass2()
print(obj._MyClass__private_var)  # Name mangling for private access


class MyClass3:
    def __init__(self):
        self._protected_var = "This is protected"

obj = MyClass3()
print(obj._protected_var)  # Accessing protected_var (convention, not strict enforcement)
