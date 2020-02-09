# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
# 2, 3, 5, 7 are prime numbers as they do not have any other factors. But 6 is not prime (composite) since, 2 x 3 = 6.

num = int(input("enter number :"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("number is not prime")
            break
    else:
        print("number is prime")

else:
    print("number is not prime")

