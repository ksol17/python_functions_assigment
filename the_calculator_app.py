# Task 1: Create functions for each arithmetic operation.
def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
#  Task 3:  Ensure your code can handle division by zero and other potential errors. 
#  So if you divide by 0, there is error handling set up to prevent an error from showing in the console.    
elif operation == "/":
    if num2 == 0:
        result = "Cannot divide by zero"
    else: 
        result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)