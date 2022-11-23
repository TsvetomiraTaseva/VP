number = input("Enter a number: ")


def is_number_palindrome(number):
    new_num = str(number)
    reversed_num = new_num[::-1]
    if number != reversed_num:
        return 0
    elif number == reversed_num:
        return 1


print(f"{is_number_palindrome(number)}")


