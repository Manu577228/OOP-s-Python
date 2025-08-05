# Data hiding in Python is the concept of restricting access to class members from outside the class.
# Python uses name mangling (prefixing with __) to achieve this.

# Prefixing a variable or method with __ makes it private.
# It's not truly private (like in Java/C++), but name-mangled to prevent direct access.
# Can still be accessed using _ClassName__var (not recommended).
# Promotes encapsulation and prevents accidental modification.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    
acc = BankAccount("Bharadwaj", 150)

print("Balance:", acc.get_balance())

try:
    print(acc.__balance)
except AttributeError:
    print("Cannot access __balance directly!")

print("Force access:", acc._BankAccount__balance)