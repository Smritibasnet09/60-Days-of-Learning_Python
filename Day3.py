"""
Day 3 - Functions in Python 🚀
Function Basics, Parameters & Return Values
"""

print("\n Python Functions")

# Simple Function
print("\n Simple Function")

def greet():
    print("Hello, Welcome to Python!")

greet()

# Function with Parameters
print("\n Function with Parameters")

def introduce(name):
    print(f"Hello, {name}!")

introduce("Smriti")

# Function with Return Value
print("\n Function with Return Value")

def add(a, b):
    return a + b

result = add(10, 5)

print("Addition:", result)

# Function with Multiple Parameters
print("\n Multiple Parameters")

def student_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student_info("Smriti", 20)

# Default Parameter
print("\n Default Parameters")

def country(name="Nepal"):
    print(f"Country: {name}")

country()
country("Japan")


# -----------------------------
# Practice Questions
# -----------------------------

# Even or Odd Function
print("\n Even or Odd Function")

def check_even_odd(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_even_odd(8)

# Simple Calculator Function
print("\n Simple Calculator Function")

def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)

calculator(10, 5)

# Square of a Number
print("\n Square of a Number")

def square(number):
    return number * number

print(square(4))

# Greeting User
print("\n Greeting User")

def greeting(name):
    print(f"Good Morning, {name}")

greeting("Smriti")

# Maximum Number
print("\n Maximum Number")

def maximum(a, b):
    if a > b:
        print(a, "is greater")
    else:
        print(b, "is greater")

maximum(20, 15)