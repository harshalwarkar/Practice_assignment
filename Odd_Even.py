# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
num = int(input("enter number : "))

if num > 0:
    for i in range(1, num):
        print(num)
        if num % 2 == 0:
            print("number is even")
            break
    else:
        print(num)
        print("number is odd")

else:
    print(num)
    print("please enter valid input")

# -------------------------------------------------
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))





