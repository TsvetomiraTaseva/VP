b = input("Enter square, rectangle or triangle: ")
#area = 0
if b == "square":
    def area_square(a):
        a = float(input("Enter a num: "))
        area = a * a
        return area
print(f"Area = {area_square(b)}")

elif b == "rectangle":
    def area_rectangle(a, b):
         a = float(input("Enter a num:  "))
         b = float(input("Enter a second num: "))
        area = a * b
         return area
print(f"Area = {area_rectangle(b)}")

