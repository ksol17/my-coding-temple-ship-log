# Ask the user to enter two numbers.
# Ask the user to choose an operation (addition, substraction, multiplication, or division)
# Perform the operation and display the result.
# Use a 'try-except' block to handle 'ValueError' and 'TypeError' exceptions.
# No matter what happens, thank the user for using the calculator in a 'finally' block.


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")


def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op in operations:
            return op
        print("Invalid operation. Please choose +, -, *, /.")

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

try:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    print(f"The result is: {result}")
except TypeError:
    print("An unexpected type error occurred.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Thank you for using the calculator!")