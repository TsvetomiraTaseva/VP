number = int(input("Enter number to find number!: "))
result_of_numbers = 1

for i in range(1, number + 1):
    result_of_numbers = i * result_of_numbers

print(result_of_numbers)