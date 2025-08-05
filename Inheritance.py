# Inheritance in Python is an OOP feature where a child class inherits attributes and methods from a parent class.
# It promotes code reusability and allows extending or customizing existing classes.

# Defined by passing the parent class name inside parentheses: class Child(Parent):
# Child class inherits all properties of the parent class.
# Child class can also add new methods or override existing ones.
# Types of inheritance: Single, Multiple, Multilevel, Hierarchical, Hybrid.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand;

    def start(self):
        print(f"{self.brand} vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

c = Car("BMW", "M1")
c.start()
c.display()
