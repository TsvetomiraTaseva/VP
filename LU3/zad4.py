a = int(input("Enter a number: "))
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print("The num is not prime number")
            break
    else:
        print("The num is prime number")

