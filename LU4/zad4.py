number = int(input("Enter a number of elements: "))
dict_num = {}
list_of_numbers = list(range(1, number + 1))
for i in range(0, len(list_of_numbers)):
    dict_num[list_of_numbers[i]] = list_of_numbers[len(list_of_numbers) - 1 - i]
print(list_of_numbers)
print(dict_num)
