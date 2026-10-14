# Methods in the python are 3 types :
# instance methods
# class methods
# static methods


# Common  built-methods in Python 
# String	upper(), lower(), split(), replace()	Modify or process text
# List	append(), insert(), remove(), sort()	Manage list elements
# Dictionary	keys(), values(), items(), get()	Access dictionary data
# Set	add(), remove(), union()	Manage unique elements
# File	read(), write(), close()	Work with files

# Setter and Getter methods :
#  Setter : Used to set the values  .Like we can update the value
#  Getter : Used to get the value ,We can read the value

# Other important methods for interviews
# - Constructor: __init__() — initializes an object.
# - Magic/Dunder methods: __str__(), __len__(), __repr__() — define special object behavior.
# - Getter and setter methods: Used to retrieve or update attribute values, often with properties.
# - Abstract methods: Define methods that subclasses are expected to implement, commonly using Python's abc module.


# Instance methods 
#  1. Instance Method
# Works with object-specific data using self.
# This is the usefull for intailaizing the variable  and it acts as a constructor .

class Employee:
    def display(self):
        print("Hello Employee")

e = Employee()
e.display()

#  2 .Class Method
# Works with class-level data using cls. It uses the @classmethod decorator.

class Employee:
    company = "Cisco"

    @classmethod
    def show_company(cls):
        print(cls.company)

Employee.show_company()

# Static Method
# A utility method that doesn't automatically receive self or cls. It uses @staticmethod.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))


#  Setter and getter methods 
class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("Invalid salary!")

e = Employee(50000)

print(e.get_salary())  

e.set_salary(60000)
print(e.get_salary())  

e.set_salary(-1000)    



#  Example for methods 
class Student:
    school = "Panchavati Vidyalaya"

    def __init__(self,name,roll,batch):
        self.name = name
        self.roll = roll
        self.batch = batch

    def details(self):
        print(self.name,self.roll,self.batch)

    @classmethod
    def info(cls):
        print(cls.school)

    @staticmethod
    def subj(a,b):
        print(f'The subjects are {a}, {b}')


s1 = Student("Kittu",123,"SSC")

s2 = Student("Kittu",12,"Class 9")

s1.details()

s2.details()

Student.info()

Student.subj("Telugu","English")
