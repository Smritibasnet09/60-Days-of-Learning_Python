"""
Day 8 - Exception Handling in Python 🚀
try, except, else & finally
"""

print("\n Python Exception Handling")

# Basic try-except
print("\n Basic try-except")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except:
    print("Invalid Input!")

# Handling Division Error
print("\n Division Error Handling")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")

# Using else
print("\n Using else")

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Invalid age!")

else:
    print("Age saved successfully.")

# Using finally
print("\n Using finally")

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found!")

finally:
    print("Program Finished.")

# Multiple Exceptions
print("\n Multiple Exceptions")

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ValueError:
    print("Invalid Number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")


# -----------------------------
# Practice Questions
# -----------------------------

# Simple Calculator with Exception Handling
print("\n Simple Calculator")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", num1 + num2)

except ValueError:
    print("Please enter numbers only!")

# Password Length Checker
print("\n Password Length Checker")

try:
    password = input("Enter password: ")

    if len(password) < 6:
        raise ValueError("Password too short!")

    print("Password Accepted")

except ValueError as error:
    print(error)

# File Reader
print("\n File Reader")

try:
    with open("notes.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist!")

# Number Checker
print("\n Number Checker")

try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

except ValueError:
    print("Invalid Input!")

# Safe List Access
print("\n Safe List Access")

numbers = [10, 20, 30]

try:
    index = int(input("Enter index number: "))
    print(numbers[index])

except IndexError:
    print("Index out of range!")

except ValueError:
    print("Invalid Input!")