
# ==========================================
# LEARNING 1: PYTHON FUNCTIONS
# ==========================================

# 1. Simple Function

def greet():
    print("Hello Smriti!")
    print("Welcome to Python Learning.")

greet()


# 2. Function with Parameters

def greet_user(name):
    print(f"Hello, {name}! Keep learning.")

greet_user("Smriti")
greet_user("Python Developer")


# 3. Function with Two Parameters

def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

add_numbers(10, 20)
add_numbers(50, 30)


# 4. Function Using Return

def square(number):
    return number * number

answer = square(5)

print("Square:", answer)


# 5. Function with Conditions

def check_age(age):

    if age >= 18:
        return "You are an adult."

    else:
        return "You are a minor."


print(check_age(21))
print(check_age(15))


# 6. Function with Default Arguments

def student_info(name, course="Computer Science"):
    print("Name:", name)
    print("Course:", course)


student_info("Smriti")
student_info("Ram", "Information Technology")


# 7. Function to Find the Largest Number

def find_largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


print("Largest:", find_largest(10, 25, 15))


# ==========================================
# END OF LEARNING 1
# ==========================================
