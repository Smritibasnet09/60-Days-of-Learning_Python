"""
Day 10 - Object-Oriented Programming in Python 🚀
Classes, Objects & Methods
"""

print("\n Python OOP Basics")

# Creating a Class
print("\n Creating a Class")

class Student:
    name = "Smriti"
    course = "Python"

student1 = Student()

print(student1.name)
print(student1.course)

# Using Constructor
print("\n Using Constructor")

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Smriti", 20)

print(person1.name)
print(person1.age)

# Creating Methods
print("\n Creating Methods")

class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

car1 = Car("Tesla")

car1.start()

# Multiple Objects
print("\n Multiple Objects")

class Laptop:

    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

laptop1 = Laptop("Dell", "16GB")
laptop2 = Laptop("HP", "8GB")

print(laptop1.brand, laptop1.ram)
print(laptop2.brand, laptop2.ram)

# Updating Object Values
print("\n Updating Object Values")

class User:

    def __init__(self, username):
        self.username = username

user1 = User("smriti123")

print("Before Update:", user1.username)

user1.username = "python_smriti"

print("After Update:", user1.username)


# -----------------------------
# Practice Questions
# -----------------------------

# Student Information System
print("\n Student Information System")

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("Smriti", 20)

student1.display()

# Employee Class
print("\n Employee Class")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Ram", 50000)

print(employee1.name)
print(employee1.salary)

# Book Class
print("\n Book Class")

class Book:

    def __init__(self, title):
        self.title = title

    def read(self):
        print(f"You are reading {self.title}")

book1 = Book("Python Basics")

book1.read()

# Mobile Class
print("\n Mobile Class")

class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mobile1 = Mobile("Samsung", 30000)

print(mobile1.brand)
print(mobile1.price)

# Bank Account
print("\n Bank Account")

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Updated Balance:", self.balance)

account1 = BankAccount(1000)

account1.deposit(500)