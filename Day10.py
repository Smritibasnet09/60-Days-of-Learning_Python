"""
Day 11 - Advanced OOP in Python 🚀
Inheritance, Encapsulation & Method Overriding
"""

print("\n Advanced OOP in Python")

# Inheritance
print("\n Inheritance")

class Animal:

    def sound(self):
        print("Animals make sounds")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog1 = Dog()

dog1.sound()
dog1.bark()

# Method Overriding
print("\n Method Overriding")

class Bird:

    def fly(self):
        print("Bird can fly")

class Penguin(Bird):

    def fly(self):
        print("Penguin cannot fly")

bird1 = Penguin()

bird1.fly()

# Encapsulation
print("\n Encapsulation")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

account1 = BankAccount(5000)

account1.show_balance()

# Using super()
print("\n Using super()")

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

student1 = Student("Smriti", "Python")

print(student1.name)
print(student1.course)

# Polymorphism
print("\n Polymorphism")

class Cat:

    def sound(self):
        print("Cat says Meow")

class Cow:

    def sound(self):
        print("Cow says Moo")

animals = [Cat(), Cow()]

for animal in animals:
    animal.sound()


# -----------------------------
# Practice Questions
# -----------------------------

# Vehicle Inheritance
print("\n Vehicle Inheritance")

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):

    def ride(self):
        print("Bike is Riding")

bike1 = Bike()

bike1.start()
bike1.ride()

# Employee & Manager
print("\n Employee & Manager")

class Employee:

    def work(self):
        print("Employee Working")

class Manager(Employee):

    def manage(self):
        print("Manager Managing Team")

manager1 = Manager()

manager1.work()
manager1.manage()

# Private Variable Example
print("\n Private Variable Example")

class User:

    def __init__(self):
        self.__password = "python123"

    def access(self):
        print("Access Granted")

user1 = User()

user1.access()

# Shape Polymorphism
print("\n Shape Polymorphism")

class Circle:

    def draw(self):
        print("Drawing Circle")

class Square:

    def draw(self):
        print("Drawing Square")

shapes = [Circle(), Square()]

for shape in shapes:
    shape.draw()

# Student Details
print("\n Student Details")

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Smriti", 90)

student1.display()