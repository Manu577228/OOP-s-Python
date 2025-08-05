# An object is an instance of a class — it is the actual implementation based on the class blueprint.
# Each object holds its own state (attributes) and can use the class's methods.

# You create an object by calling the class like a function: obj = ClassName().
# Multiple objects of the same class can hold different data.
# Each object can access and modify its own data.

class Car:
   def __init__(self, brand, year):
     self.brand = brand
     self.year = year

   def display(self):
        print("Brand", self.brand)
        print("Year", self.year)

car1 = Car("BMW", 2025)
car2 = Car("Honda", 2022)

car1.display()
car2.display()

