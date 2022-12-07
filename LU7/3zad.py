from math import sqrt
try:
    number = int(input("Enter number: "))
    if number < 0:
        raise ValueError
    print(sqrt(number))
except ValueError:
    print("The number is negative")
finally:
    print("Good Bye")
