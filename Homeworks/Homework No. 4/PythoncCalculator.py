# This function adds two numbers
def multiply(first_number, second_number):
    return first_number * second_number

# This function subtracts two numbers
def divide(first_number, second_number):
    if second_number == 0:
        raise Exception("You can't divide by 0")
    return first_number / second_number

# This function multiplies two numbers
def add(first_number, second_number):
    return first_number + second_number

# This function divides two numbers
def subtract(first_number, second_number):
    return first_number - second_number

# This function finds percentage among two numbers
def percent(first_number, second_number):
    if second_number == 0:
        raise Exception("You can't divide by 0")
    return (first_number / second_number) * 100

def operational_menu(result):

    outputLine = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    result = str(result)
    for i in range(len(result)):
        outputLine[len(outputLine) - 1 - i] = (result[len(result) - 1 - i])

    output = ''.join(outputLine)

    print('--------------------')
    print('|Standard         X|')
    print('|                  |')
    print('|                  |')
    print(f'|       {output}|')
    print('--------------------')
    print('|      C      || / |')
    print('| 7 || 8 || 9 || * |')
    print('| 4 || 5 || 6 || + |')
    print('| 1 || 2 || 3 || - |')
    print('| 0 || . || % || = |')
    print('--------------------')

result = 0

# Basic user interface
while True:

    commands = ['+', '-', '/', '*', '%']

    # Operational menu
    operational_menu(result)

    command = input("Enter a command: ")
    if command == 'X':
        break

    if command in commands:
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter a number")
            continue

        if command == '+':
            result = add(first_number, second_number)
        elif command == '-':
            result = subtract(first_number, second_number)
        elif command == '/':
            try:
                result = divide(first_number, second_number)
            except Exception as e:
                print(e)
        elif command == '*':
            result = multiply(first_number, second_number)
        elif command == '%':
            try:
                result = percent(first_number, second_number)
            except Exception as e:
                print(e)

        # The result from the operation
        operational_menu(result)

        next_calculation = input("Would you like to do a new calculation?")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")
