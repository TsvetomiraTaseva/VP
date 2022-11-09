numbers = int(input("How many numbers will receive: "))
i = 1
sum = 0
while i <= numbers:
    num = int(input(f"Enter a num {i}: "))
    i += 1
    sum += num

print(sum)