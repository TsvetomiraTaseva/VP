list_sum = []


def sum_list(lst):
    sum_elements = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum_elements += i
    return sum_elements


print(sum_list(["asd", "-"]))

