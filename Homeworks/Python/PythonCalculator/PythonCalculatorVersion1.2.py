class Calculator:
    # This function adds two numbers
    def multiply(self, first_number, second_number):
        return first_number * second_number

    # This function subtracts two numbers
    def divide(self, first_number, second_number):
        if second_number == 0:
            raise Exception("You can't divide by 0")
        return first_number / second_number

    # This function multiplies two numbers
    def add(self, first_number, second_number):
        return first_number + second_number

    # This function divides two numbers
    def subtract(self, first_number, second_number):
        return first_number - second_number

    # This function finds percentage among two numbers
    def percent(self, first_number, second_number):
        if second_number == 0:
            raise Exception("You can't divide by 0")
        return (self, first_number / second_number) * 100

#Graphical user interface
class OperationalMenu:

    def run(self, result):
        outputLine = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        #Converting result into string
        result = str(result)
        for i in range(len(result)):
            outputLine[len(outputLine) - 1 - i] = (result[len(result) - 1 - i])

        #Joining result as one string
        output = ''.join(outputLine)

        #Displaying the result
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


class Engine:
    #Constructor
    def __init__(self, operational_menu, calculator):
        self.operational_menu = operational_menu
        self.calculator = calculator

    #Buisness logic
    def run(self):

        result = 0

        while True:

            commands = ['+', '-', '/', '*', '%', 'C']

            self.operational_menu.run(result)

            command = input("Enter a command: ")
            if command == 'X':
                break
            elif command == 'C':
                result = 0
                self.operational_menu.run(result)
                continue

            if command in commands:
                try:
                    first_number = float(input("Enter first number: "))
                    second_number = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter only numbers")
                    continue

            if command == '+':
                result = self.calculator.add(first_number, second_number)
            elif command == '-':
                result = self.calculator.subtract(first_number, second_number)
            elif command == '/':
                try:
                    result = self.calculator.divide(first_number, second_number)
                except Exception as e:
                    print(e)
            elif command == '*':
                result = self.calculator.multiply(first_number, second_number)
            elif command == '%':
                try:
                    result = self.calculator.percent(first_number, second_number)
                except Exception as e:
                    print(e)

            # Operational menu
            self.operational_menu.run(result)

            next_calculation = input("Would you like to do a new calculation? Choose: [yes/no]")
            if next_calculation == "yes":
                continue
            elif next_calculation == "no":
                break
        else:
            print("Invalid input")

# Main
operational_menu = OperationalMenu()
calculator = Calculator()
engine = Engine(operational_menu, calculator)

engine.run()