# What is Encapsulation?
# Encapsulation is an OOP concept that combines data (variables) and methods (functions) into a single class and
# controls how that data is accessed or modified.

# Real-world example: ATM
# - You can check your balance.
# - You can withdraw money.
# - You cannot directly access the bank's internal database.
# - The ATM controls how your money is accessed.


# Access modifiers in Python
# Type	     Syntax	           Meaning
# Public	  self.name	      Accessible normally
# Protected   (convention)	  self._name	Intended for internal use and subclasses
# Private-like	 self.__name	  Uses name mangling to discourage direct access


# In Python, encapsulation helps protect data and provides controlled access through methods.

# Encapsulation	                          v/s                     Abstraction
# Bundles data and methods and controls access                 Hides implementation details
# Focuses on data protection and controlled modification	   Focuses on showing essential features

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())  


