try:
    print(number)
except:
    print("An error has occurred!!!")

num1 = 39
num2 = 0
# print(num1/num2)

try:
    print(num1/num2)
except:
    print("A Zero Division error has occurred!!!")
finally:
    print("Success!!!")
