# Project: Simple Calculator using function
# Defining a function
def add(x, y):
    """This function returns an addition"""
    return x + y
def subtract(x, y):
    """This function returns a subtraction"""
    return x - y
def multiply(x, y):
    """This function returns a multiplication"""
    return x * y
def divide(x, y):
    """This function returns a division"""
    return x / y 
def floorDiv(x, y):
    """This function returns a floor-division"""
    return x // y
def remainder(x, y):
    """This function returns a remainder"""
    return x % y


# Creating a menu
print("Select an operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Floor Division")
print("6.Remainder")
print("*" * 80)


# Requesting an input
choice = input("Enter choice (1/2/3/4/5/6): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


# Using simple arithmetics and making decisions using If_Statment
if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == "5":
    print(num1, "//", num2, "=", floorDiv(num1, num2))
elif choice == "6":
    print(num1, "%", num2, "=", remainder(num1, num2))
else:
    print("Invalid input")