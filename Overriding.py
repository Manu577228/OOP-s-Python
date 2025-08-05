# Overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
# It enables custom behavior in the child class while reusing the structure of the parent class.

# Used in inheritance.
# If a method with the same name exists in both parent and child, the child’s version is called.
# Helps in extending or customizing the base class behavior.

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks!")

class Cat(Animal):
    def speak(self):
        print("The Cat meows!")

a = Animal()
d = Dog()
c = Cat()

a.speak()
d.speak()
c.speak()

