"""
Day 14 - Student Management System 
Using Lists, Dictionaries, Functions and Loops
"""

students = []

def add_student():

    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student Added Successfully!")

def view_students():

    if len(students) == 0:
        print("No Students Found.")
        return

    for student in students:
        print("\nStudent Details")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")