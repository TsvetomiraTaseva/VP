import string

base = string.digits + string.ascii_uppercase
number = 27102022
binary_number = ""
hex_number = ""

while number != 0:
    binary_number += str(number % 2)
    number //= 2

number = 27102022
while number != 0:
    hex_number += base[number % 16]
    number //= 16

print(binary_number[::-1])
print(hex_number[::-1])
