number = int(input("Enter number: "))
end_number = int(input("Enter last number: "))

for i in range(number, end_number + 1):
    count_num = 0
    for k in range (i):
        if i % (k + 1) == 0:
            count_num += 1
    if count_num == 2:
        print(i)