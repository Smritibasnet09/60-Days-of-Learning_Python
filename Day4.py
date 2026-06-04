"""
Day 4 - Strings in Python 
String Basics, Methods & Operations
"""

print("\n Python Strings")

# String Basics
print("\n String Basics")

name = "Smriti"

print(name)
print(type(name))

# String Concatenation
print("\n String Concatenation")

first_name = "Smriti"
last_name = "Basnet"

full_name = first_name + " " + last_name

print(full_name)

# String Length
print("\n String Length")

language = "Python"

print("Length:", len(language))

# String Methods
print("\n String Methods")

text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())

# String Indexing
print("\n String Indexing")

word = "Python"

print(word[0])
print(word[2])
print(word[-1])

# String Slicing
print("\n String Slicing")

message = "LearningPython"

print(message[0:8])
print(message[8:14])

# f-Strings
print("\n f-Strings")

name = "Smriti"
goal = "AI Engineer"

print(f"My name is {name} and I want to become an {goal}.")


# -----------------------------
# Practice Questions
# -----------------------------

# Reverse a String
print("\n Reverse a String")

text = input("Enter a word: ")

print(text[::-1])

# Count Characters
print("\n Count Characters")

word = input("Enter a word: ")

print("Total Characters:", len(word))

# Check Palindrome
print("\n Palindrome Checker")

text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Username Generator
print("\n Username Generator")

first = input("Enter first name: ")
last = input("Enter last name: ")

username = first + "_" + last

print("Username:", username)

# Replace Word
print("\n Replace Word")

sentence = "I love Java"

print(sentence.replace("Java", "Python"))