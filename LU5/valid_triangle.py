def is_valid_triangle(a, b, c):
    a1 = a * a
    b1 = b * b
    c1 = c * c
    if a1 + b1 == c1:
        return True
    else:
        return False


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

can_triangle_exist = is_valid_triangle(a, b, c)
print(can_triangle_exist)
print(is_valid_triangle(a, b, c))
