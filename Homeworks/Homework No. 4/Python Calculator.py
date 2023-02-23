
# This function adds two numbers
def multiply(first_number, second_number):
    return first_number * second_number

# This function subtracts two numbers
def divide(first_number, second_number):
    return first_number / second_number

# This function multiplies two numbers
def add(first_number, second_number):
    return first_number + second_number

# This function divides two numbers
def subtract(first_number, second_number):
    return first_number - second_number

# Basic user interface
while True:
    # Operational menu
    print("Operational Menu:")
    print("+")
    print("-")
    print("/")
    print("*")

    command = input("Enter a command: ")
    if command in ('+', '-', '/', '*'):
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
            result = divide(first_number, second_number)
        elif command == '*':
            result == multiply(first_number, second_number)

        # The result from the operation
        print(f"Result: {result}")

        next_calculation = input("Would you like to do a new calculation?")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")
