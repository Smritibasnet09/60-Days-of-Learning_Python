"""
Day 6 - Dictionaries & Sets in Python 🚀
Dictionary Operations, Methods & Set Basics
"""

print("\n Python Dictionaries & Sets")

# Dictionary Basics
print("\n Dictionary Basics")

student = {
    "name": "Smriti",
    "age": 20,
    "course": "Python"
}

print(student)

# Accessing Dictionary Values
print("\n Accessing Dictionary Values")

print(student["name"])
print(student["course"])

# Adding New Item
print("\n Adding New Item")

student["college"] = "Sunway College"

print(student)

# Updating Values
print("\n Updating Values")

student["age"] = 21

print(student)

# Dictionary Methods
print("\n Dictionary Methods")

print(student.keys())
print(student.values())
print(student.items())

# Loop Through Dictionary
print("\n Loop Through Dictionary")

for key, value in student.items():
    print(key, ":", value)

# Set Basics
print("\n Set Basics")

numbers = {1, 2, 3, 4, 5}

print(numbers)

# Adding Elements to Set
print("\n Adding Elements to Set")

numbers.add(6)

print(numbers)

# Removing Duplicate Values
print("\n Removing Duplicates Using Set")

data = [1, 2, 2, 3, 4, 4, 5]

unique_data = set(data)

print(unique_data)


# -----------------------------
# Practice Questions
# -----------------------------

# Student Information
print("\n Student Information")

student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "course": input("Enter course: ")
}

print(student)

# Favorite Foods Set
print("\n Favorite Foods Set")

foods = {"Momo", "Pizza", "Burger"}

foods.add("Pasta")

print(foods)

# Word Meaning Dictionary
print("\n Word Meaning Dictionary")

words = {
    "Python": "Programming Language",
    "AI": "Artificial Intelligence",
    "API": "Application Programming Interface"
}

print(words["AI"])

# Count Unique Numbers
print("\n Count Unique Numbers")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)
print("Total Unique Numbers:", len(unique_numbers))

# Simple Login System
print("\n Simple Login System")

user = {
    "username": "admin",
    "password": "python123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username == user["username"] and password == user["password"]:
    print("Login Successful")
else:
    print("Invalid Credentials")