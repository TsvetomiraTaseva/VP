def max_of_two(a, b):
    if a == b:
        return a
    elif type(a) != int or type(a) != float:
        return b
    elif type(b) != int or type(b) != float:
        return a
    elif (type(a) != int or type(a) != float) and (type(b) != int or type(b) != float):
        return
    elif float(a) > float(b):
        return a
    elif float(b) > float(a):
        return b

    
print(max_of_two('a', 5))