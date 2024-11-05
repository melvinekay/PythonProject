print("Calculator")
print("Menu")
# def inp():
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def operation():
    print("Select operation to work with: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    select = int(input("Enter your choice: "))
    if select == 1:
        add()
    elif select == 2:
        subtract()
    elif select == 3:
        multiply()
    elif select == 4:
        divide()
    elif select == 5:
        modulus()
    else:
        print("Thank you for using the calculator!")

def add():
    print(f"Addition = {num1 + num2}")
def subtract():
    print(f"Subtraction = {num1 - num2}")
def multiply():
    print(f"Multiplication  = {num1 * num2}")
def divide():
    print(f"Division = {num1 / num2}")
def modulus():
    print(f"Modulus  = {num1 % num2}")
def main():
    operation()
main()
