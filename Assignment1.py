
'''### Assignment 1: Coding Challenge

- Implement a simple command-line application that performs basic arithmetic operations (addition, subtraction, multiplication, and division).
- The application should prompt the user to enter two numbers and the desired operation, then display the result.
- Ensure the application handles invalid inputs and provides appropriate error messages.
- Bonus: Implement additional features, such as support for more complex operations or the ability to save and load previous calculations.
'''
import math

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            return "Error: Cannot divide by zero"
        result = x / y
        self.history.append(f"{x} / {y} = {result}")
        return result

    def exponentiation(self, x, y):
        result = x ** y
        self.history.append(f"{x} ^ {y} = {result}")
        return result

    def square_root(self, x):
        if x < 0:
            return "Error: Cannot calculate square root of a negative number"
        result = math.sqrt(x)
        self.history.append(f"sqrt({x}) = {result}")
        return result

    def sin(self, x):
        result = math.sin(math.radians(x))
        self.history.append(f"sin({x}) = {result}")
        return result

    def cos(self, x):
        result = math.cos(math.radians(x))
        self.history.append(f"cos({x}) = {result}")
        return result

    def tan(self, x):
        result = math.tan(math.radians(x))
        self.history.append(f"tan({x}) = {result}")
        return result

    def save_history(self, filename="calculator_history.txt"):
        with open(filename, "w") as file:
            for entry in self.history:
                file.write(entry + "\n")

    def load_history(self, filename="calculator_history.txt"):
        try:
            with open(filename, "r") as file:
                self.history = [line.strip() for line in file]
        except FileNotFoundError:
            print("File not found. No history loaded.")

def main():
    calculator = Calculator()
    print('Welcome to the Simple Calculator App')
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input('Enter the operation (+, -, *, /, ^, sqrt, sin, cos, tan): ')

            if operation in ['+', '-', '*', '/']:
                num2 = float(input("Enter the second number: "))
            elif operation in ['^', 'sqrt', 'sin', 'cos', 'tan']:
                num2 = None  
            else:
                print('Error: Invalid operation. Please enter one from the given options only.')
                continue

            if operation == '+':
                result = calculator.add(num1, num2)
            elif operation == '-':
                result = calculator.subtract(num1, num2)
            elif operation == '*':
                result = calculator.multiply(num1, num2)
            elif operation == '/':
                result = calculator.divide(num1, num2)
            elif operation == '^':
                result = calculator.exponentiation(num1, num2)
            elif operation == 'sqrt':
                result = calculator.square_root(num1)
            elif operation == 'sin':
                result = calculator.sin(num1)
            elif operation == 'cos':
                result = calculator.cos(num1)
            elif operation == 'tan':
                result = calculator.tan(num1)
            else:
                print('Error: Invalid operation. Please enter one from the given options only.')
                continue
            
            print("Result:", result)

            calculator.save_history()

        except ValueError:
            print('Error: Invalid input. Please enter numeric value')
        
        except Exception as e:
            print('An error occurred:', e)
        
        choice = input("Do you want to load calculation history? (yes/no): ")
        if choice.lower() == 'yes':
            calculator.load_history()
            print("Calculation history:")
            for entry in calculator.history:
                print(entry)
                
        choice = input("Do you want to perform another calculation or load history? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the Simple Calculator App!")
            break

if __name__ == '__main__':
    main()
