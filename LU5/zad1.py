list_numbers = []


def input_nums(n):
    for i in range(n):
        element = input("Enter a number: ")
        if element.isnumeric():
            list_numbers.append(element)
    return list_numbers


print(input_nums(3))

