number = int(input("Enter range number: "))
dict_1 = {}
for i in range(0, number):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict_1[key] = value

number1 = int(input("Enter another number: "))
list_1 = []
for i in range(0, number1):
    value = input("Enter value: ")
    list_1.append(value)

print(dict_1)
print(list_1)

for i in range(0, number1):
    for key in dict_1:
        if list_1[i] == key:
            list_1[i] = dict_1[key]

