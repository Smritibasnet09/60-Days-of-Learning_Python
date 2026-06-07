"""
Day 7 - File Handling in Python 🚀
Reading, Writing & Appending Files
"""

print("\n Python File Handling")

# Writing to a File
print("\n Writing to a File")

file = open("sample.txt", "w")

file.write("Hello, Welcome to Python File Handling!")

file.close()

print("Data written successfully.")

# Reading a File
print("\n Reading a File")

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

# Appending Data
print("\n Appending Data")

file = open("sample.txt", "a")

file.write("\nThis is a new line added.")

file.close()

print("Data appended successfully.")

# Reading Updated File
print("\n Updated File Content")

file = open("sample.txt", "r")

print(file.read())

file.close()

# Using with open()
print("\n Using with open()")

with open("sample.txt", "r") as file:
    print(file.read())


# -----------------------------
# Practice Questions
# -----------------------------

# Create Notes File
print("\n Create Notes File")

note = input("Write a note: ")

with open("notes.txt", "w") as file:
    file.write(note)

print("Note saved successfully.")

# Read Notes File
print("\n Read Notes File")

with open("notes.txt", "r") as file:
    print(file.read())

# Add More Notes
print("\n Add More Notes")

extra_note = input("Add another note: ")

with open("notes.txt", "a") as file:
    file.write("\n" + extra_note)

print("New note added.")

# Count Characters in File
print("\n Count Characters in File")

with open("notes.txt", "r") as file:
    content = file.read()
    print("Total Characters:", len(content))

# Simple Diary Program
print("\n Simple Diary Program")

diary = input("How was your day? ")

with open("diary.txt", "a") as file:
    file.write(diary + "\n")

print("Diary saved successfully.")