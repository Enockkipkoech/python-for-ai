import math

print("Custom functions")


def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Enock")  # Call the function with the argument "Enock"


def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)  # Call the function with arguments 5 and 3
print(f"The sum is: {result}")  # Print the result of the addition


def calculate_area(radius):
    area = math.pi * radius ** 2
    return area


area_result = calculate_area(5)  # Call the function with radius 5
print(f"The area of the circle is: {area_result}")  # Print the area


def list_items(*items):
    total = 1
    for item in items:
        total *= item
    return total


# Call the function with multiple arguments
result = list_items(2, 3, 4, 5, 6, 7, 8, 9)
print(f"The final total is: {result}")  # Print the final total
