# Methods are functions defined inside a class that operate on the objects (instances) of that class.
# They usually take self as the first parameter to access or modify the object's data.

# Defined like regular functions but inside a class.
# The first parameter is always self, referring to the instance calling the method.
# Can be of three types:
# Instance Methods: Access/modify object data.
# Class Methods: Use @classmethod and operate on class-level data.
# Static Methods: Use @staticmethod, no self or class data access.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    @classmethod
    def description(cls):
        print("This is a simple calculator class.")

    @staticmethod
    def greet():
        print("Welcome to the simple Calculator app")

calc = Calculator()

print("Add:", calc.add(10, 5))
print("Multiply:", calc.multiply(10, 5))

Calculator.description()

Calculator.greet()