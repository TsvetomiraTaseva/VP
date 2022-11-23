b = input("Enter square, rectangle or triangle: ")


def area_square(a):
    area = a ** 2
    return area


def area_rectangle(a, b):
    area = a * b
    return area


def area_triangle(a, b):
    area = (a * b)/2
    return area


if b == "square":
    a = float(input("Enter number: "))
    print(f"Area of square is {area_square(a)}")
elif b == "rectangle":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Area og rectangle is {area_rectangle(a, b)}")
elif b == "triangle":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Area og rectangle is {area_triangle(a, b)}")



