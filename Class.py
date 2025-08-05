# A class in Python is a blueprint for creating objects (instances) that encapsulate data and behavior.
# It defines properties (variables) and methods (functions) under a single logical unit.

# Defined using the class keyword.

# Typically includes a constructor (__init__) to initialize object data.

# Variables inside a class are called attributes, and functions are called methods.

# Promotes code reusability, modularity, and encapsulation.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("Bharadwaj", 31)

p1.show_info()
