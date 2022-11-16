word = input("Enter a word: ")
d = dict()
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)
