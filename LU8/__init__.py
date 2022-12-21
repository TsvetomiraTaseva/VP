from triangle import triangle
from square import square
from rectangle import rectangle
from rhombus import rhombus
from trapezoid import trapezoid

area = input("Enter a figure: ")

if area == "triangle":
    a = float(input())
    b = float(input())
    triangle(a, b)
elif area == "square":
    a = float(input())
    square(a)
elif area == "rectangle":
    a = float(input())
    b = float(input())
    rectangle(a, b)
elif area == "rhombus":
    a = float(input())
    h = float(input())
    rhombus(a, h)
elif area == "trapezoid":
    a = float(input())
    b = float(input())
    h = float(input())
    trapezoid(a, b, h)

