
def add(x, y):
    return print(x+y)


def subtract(x, y):
    return print(x-y)


def multiply(x, y):
    return print(x*y)


def division(x, y):
    return print(x/y)


print("Select Operation")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice = input("select 1/2/3/4:  ")

num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))

if choice == "1":
    add(num1, num2)

elif choice == "2":
    subtract(num1, num2)

elif choice == "3":
    multiply(num1, num2)

elif choice == "4":
    print(division(num1, num2))

else:
    print ("invalid number")







