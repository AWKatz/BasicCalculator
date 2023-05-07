# Day 10 of 100 for the Udemy Python Bootcamp
# Basic Calculator App

from art import logo

# Add
def add(n1, n2):
    """Sum of 2 input values"""
    return n1 + n2

# Subtract
def subtract(n1, n2):
    """Subtract 2 input values"""
    return n1 - n2

# Multiply
def multiply(n1, n2):
    """Multiply 2 input values"""
    return n1 * n2

# Divide
def divide(n1, n2):
    """Divides 2 input values"""
    return n1 / n2

# Create a dictionary to store values/operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    keep_alive = True

    while keep_alive:
        for operator in operations:
            print(operator)
        selected_operation = input("Pick an operator from the list: ")
        num2 = float(input("Enter the next number: "))
        calculation = operations[selected_operation]
        answer = float(calculation(num1, num2))

        print(f"{num1} {selected_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer} or type 'n' to exit: ") == "y":
            num1 = answer

        else:
            keep_alive = False

calculator()
