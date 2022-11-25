def list_avg(lst, multiplier):
    sum_elements = 0
    counter = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum_elements += i * multiplier
            counter += 1
        elif type(i) == str and i.isnumeric():
            sum_elements += float(i) * multiplier
            counter += 1
    return sum_elements / counter


print(list_avg([7, 4, "3", "j", (1, 2, "t")], 4))
