# A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400. 

year = float(input("Enter the year:"))
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")