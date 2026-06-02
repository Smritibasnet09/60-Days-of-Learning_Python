"""
Day 2 - Python Operators & Loops 🚀
Arithmetic, Relational, Assignment & Logical Operators
"""

print("\n Python Operators & Loops")

# Arithmetic Operators
print("\n Arithmetic Operators")

num1 = 10
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

# Relational / Comparison Operators
print("\n Relational Operators")

a = 20
b = 15

print("a > b :", a > b)
print("a < b :", a < b)
print("a == b :", a == b)
print("a != b :", a != b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Assignment Operators
print("\n Assignment Operators")

x = 10

print("Initial Value:", x)

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

# Logical Operators
print("\n Logical Operators")

age = 20
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

# For Loop
print("\n For Loop Example")

for i in range(1, 6):
    print("Number:", i)

# While Loop
print("\n While Loop Example")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# -----------------------------
# Practice Questions
# -----------------------------

# Multiplication Table
print("\n Multiplication Table")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Sum of Numbers
print("\n Sum of Numbers")

total = 0

for i in range(1, 6):
    total += i

print("Total Sum:", total)

# Even Numbers from 1 to 20
print("\n Even Numbers from 1 to 20")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Password Validation
print("\n Password Validation")

password = "python123"

user_input = input("Enter password: ")

while user_input != password:
    user_input = input("Wrong password. Try again: ")

print("Access Granted")

