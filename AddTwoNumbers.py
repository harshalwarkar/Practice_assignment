
num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))

addition = num1 + num2

print("sum of {a} and {b} is {c}".format(a=num1, b=num2, c=addition))
# ---------------------------------------------


def add(x, y):
    return x+y


print(add(num1, num2))
