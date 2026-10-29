
import math

# BUilt-in functions
print("Hello, World!")
print("*" * 20)

print("hey")
x = 1
print(x)


# VARIABLES
student_name = "Enock Kipkoech"
students_count = 200

print(student_name)
print(students_count)

is_published = True
print(is_published)

message = '''
This is a multi-line string.
It can span multiple lines.
'''

print(message)

len(message)  # This will return the length of the message string
print(len(message))

print(student_name.upper())  # Convert to uppercase
print(student_name.lower())  # Convert to lowercase
print(student_name.title())  # Convert to title case
print(student_name[0:9])  # Slice the string from index 0 to 9


print(student_name[0:])
print(student_name[:])

full_name = student_name + " " + "is a student."
print(full_name)

fmtd = f"{student_name} {message}."
print(fmtd)

#  String FUNCTIONS /Methods

course_name = "Python Programming"
course_name = course_name.replace(
    "Python", "Java")  # Replace "Python" with "Java"
print(course_name)
print(course_name.find("Python"))  # Find the index of the substring "Python"
print(course_name in "Python")  # Check if "Python" is in the string
print(course_name not in "Swift")  # Check if "Swift" is not in the string

# NUMBERS
x = 10
y = 3.23
Z = x + 3j

print(x, y, Z)

print(type(x))  # <class 'int'>

#  MATH
math.ceil(2.3)  # Round up to the nearest integer
math.floor(2.7)  # Round down to the nearest integer


temp = 20
if temp > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temp > 20:
    print("It's a nice day")
else:
    print("It's a cold day")

age = 45
if age >= 18:
    message = "You are an adult"
else:
    message = "You are a child"
print(message)

message = "You are an adult" if age >= 18 else "You are a child"
print(message)

# LOGICAL OPERATORS
#  AND OR NOT
high_income = True
good_credit = False
criminal_record = False
if (high_income or good_credit) and not criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# LOOP
for number in range(1, 10, 2):
    print("Attempts:", number + 1, number * "*")

successfull = True

for number in range(3):
    print("Attempt")
    if successfull:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

shopping_cart = ["apple", "banana", "mango"]
for item in shopping_cart:
    print("Shopping Cart:", f"`{item}`")

number = 10
while number > 0:
    print("Number:", number)
    number -= 1

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO:", command.upper())

# while True:
#     command = input(">")
#     if command.lower() == "quit":
#         break
#     print("ECHO:", command.upper())


# Print even numbers from 1 to 10
count = 0
for number in range(1, 10):
    if number % 2 != 0:
        continue
    count += 1
    print("Even Number:", number)
print("We have ", f"{count}", "even numbers in the range of 1 to 10")
