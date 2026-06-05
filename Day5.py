"""
Day 5 - Lists & Tuples in Python 
List Operations, Methods & Tuple Basics
"""

print("\n Python Lists & Tuples")

# List Basics
print("\n List Basics")

skills = ["Python", "AWS", "AI"]

print(skills)
print(type(skills))

# Accessing List Items
print("\n Accessing List Items")

print(skills[0])
print(skills[1])
print(skills[-1])

# Adding Items
print("\n Adding Items")

skills.append("Git")

print(skills)

# Removing Items
print("\n Removing Items")

skills.remove("AWS")

print(skills)

# List Length
print("\n List Length")

print("Total Items:", len(skills))

# Loop Through List
print("\n Loop Through List")

for skill in skills:
    print(skill)

# List Slicing
print("\n List Slicing")

numbers = [1, 2, 3, 4, 5, 6]

print(numbers[0:3])
print(numbers[3:6])

# Tuple Basics
print("\n Tuple Basics")

colors = ("Red", "Blue", "Green")

print(colors)
print(type(colors))

print(colors[0])


# -----------------------------
# Practice Questions
# -----------------------------

# Favorite Movies List
print("\n Favorite Movies List")

movies = []

movies.append(input("Enter first movie: "))
movies.append(input("Enter second movie: "))
movies.append(input("Enter third movie: "))

print("Favorite Movies:", movies)

# Sum of List Numbers
print("\n Sum of List Numbers")

numbers = [10, 20, 30, 40]

total = sum(numbers)

print("Total Sum:", total)

# Find Maximum Number
print("\n Find Maximum Number")

numbers = [5, 12, 8, 20, 3]

print("Maximum Number:", max(numbers))

# Count Items in List
print("\n Count Items in List")

fruits = ["apple", "banana", "apple", "orange"]

print("Apple Count:", fruits.count("apple"))

# Student Names
print("\n Student Names")

students = ["Ram", "Sita", "Hari"]

for student in students:
    print(student)