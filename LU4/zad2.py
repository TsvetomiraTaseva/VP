import random
s = []
list1 = []
for i in range(10):
    s.append(random.randint(0, 56))

list1.append(s[0])

for i in range(len(s) - 1):
    sum_of_elements = s[i] + s[i + 1]
    list1.append(sum_of_elements)
    list1.append(s[i + 1])


print(f"List_1: {s}")
print(f"List_2: {list1}")



