"""
Day 1 - Python Foundations 
Variables, Data Types & User Input
"""

print("\n Python Foundations")

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello {name}! You are {age} years old.")

print("\n Data Types")

language = "Python"
days = 60
progress = 1.5
is_learning = True

print(type(language))
print(type(days))
print(type(progress))
print(type(is_learning))

print("\n List Example")

skills = ["Python", "AWS", "AI"]

print(skills)

# Practice Questions

print("\n Even or Odd Checker")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


print("\n  Simple Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)


print("\n Positive or Negative Number")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")


print("\n Simple Password Check")

password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")


print("\n Grade Checker")

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")