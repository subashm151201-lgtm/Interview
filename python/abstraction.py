# What is abstraction .?
# Abstraction is the process of hiding internal implementation details and showing only the essential features to the user.
# In simple words: You know what something does, but you don't need to know how it works internally.

# Example : ATM
# When you use an ATM:
# - You enter your PIN.
# - You select an amount.
# - You receive cash.

#  How do we implement abstraction in Python?
# Python supports abstraction using the abc module (Abstract Base Classes).


# What is abstraction?	Hiding implementation details and exposing essential functionality.
# How do you achieve abstraction in Python?	Using abstract classes and abstract methods from abc.
# What is an abstract method?	A method declared in an abstract class that concrete subclasses must implement.
# Can we instantiate an abstract class?	Not while it has unimplemented abstract methods.
# What is the benefit?	Consistency, maintainability, and a clear interface.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with a button")


car = Car()
car.start()

bike = Bike()
bike.start()

# ........

from abc import ABC, abstractmethod

class ServerDiagnostic(ABC):

    @abstractmethod
    def check(self):
        pass


class CPUCheck(ServerDiagnostic):

    def check(self):
        print("Checking CPU using lscpu")


class MemoryCheck(ServerDiagnostic):

    def check(self):
        print("Checking memory using free command")


cpu = CPUCheck()
cpu.check()

memory = MemoryCheck()
memory.check()