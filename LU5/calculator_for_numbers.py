choice = input("Enter operation adding/+ subtracting/- multiplication/* or division/: ")
a = int(input("Enter number: "))
b = int(input("Enter second number: "))


def action(a, b):
    if choice == "adding" or choice == "+":
        return a + b
    elif choice == "subtracting" or choice == "-":
        return a - b
    elif choice == "multiplication" or choice == "*":
        return a * b
    elif choice == "division" or choice == "/":
        return a / b


print(f"Result from calculator is: {action(a, b)}")
