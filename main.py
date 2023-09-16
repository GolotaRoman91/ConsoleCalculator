def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error cant divide to 0!"
    return x / y

while True:
    print("Choose operation:")
    print("1 Add")
    print("2 substract")
    print("3 multiply")
    print("4 divide")
    print("5 exit")

    choice = input("Type number of operation:")

    if choice == '5':
        print("Exit from calculator")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Incorrect input. Try again")
        continue

    num1 = float(input("Type the number: "))
    num2 = float(input("Type the number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtraction(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))