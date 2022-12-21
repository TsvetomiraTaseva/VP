from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from devision import division

method = input("Enter addition/ +; subtraction/-; multiplication/* or division/ / ")
a = float(input())
b = float(input())
if method == "addition" or method == "+":
    addition(a, b)
elif method == "subtraction" or method == "-":
    subtraction(a, b)
elif method == "multiplication" or method == "*":
    multiplication(a, b)
elif method == "division" or method == "/":
    division(a, b)