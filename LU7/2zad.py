
try:
    file = open("vgk.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("This file does not exist")
else:
    file.close()
