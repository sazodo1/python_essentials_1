# basic calc

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

choice = input("\n Enter 'a' for addition, 's' for subtraction, 'm' for multiplication and 'd' for division : ")

num1 = int(input('\n Input your first number: '))
num2 = int(input('\n Input your second number: '))

if choice == 'a':
    print(num1, " + ", num2, " = ", add(num1, num2))
elif choice == 's':
    print(num1, " - ", num2, " = ", subtract(num1, num2))
elif choice == 'm':
    print(num1, " * ", num2, " = ", multiplication(num1, num2))
elif choice == 'd':
    print(num1, " / ", num2, " = ", division(num1, num2))
else:
    print("Invalid option")

