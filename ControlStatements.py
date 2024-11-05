temp = 45

if temp > 25:
    print("It is too cold")
else:
    print("It is cold")

# A python program that checks three returns the smallest
# num1 = 30
# num2 = 67
# num3 = 56
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number.")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number.")
else:
    print(num3, "is the smallest number.")

#A program to check whether a number is even or odd
number = 67
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")