number = int(input("Enter number range: "))
list_of_numbers = []

for i in range(0, number):
    second_number = int(input("Enter number: "))
    list_of_numbers.append(second_number)
print(list_of_numbers)

for i in range(0, number):
    third_number = int(input("Enter 0 or 1: "))
    if third_number == 0:
        if i % 2 == 0:
            list_of_numbers[i] = list_of_numbers[i] + 5
    elif third_number == 1:
        if i % 2 != 0:
            list_of_numbers[i] = list_of_numbers[i] + 10
    else:
        print("Invalid number:")

print(list_of_numbers)