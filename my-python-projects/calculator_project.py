import os
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print("This is a calculator📱")

    first_number = int(input("Enter first number: "))
    for key in operation_dict:
        print(key)

    continue_flag = True
    while continue_flag:
        operator = input("Pick an operater: ")
        second_number = int(input("Enter secend number: "))
        calculater = operation_dict[operator]
        output = calculater(first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {output}")
        should_continue = input(f"Enter 'yes' to continue calculation with number {output} or 'no' to exit Or 'new' to start a new calculation: ").lower()
        if should_continue == 'yes':
            first_number = output
        elif should_continue == 'new':
            continue_flag = False
            os.system('clear')
            calculator()
        else:
            continue_flag = False
            print("*****************************")
            print("******")
            print("bye")
calculator()