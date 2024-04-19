from calculator_art import *

operations = ['+', '-', '*', '/']

def calculate(n1, n2, operation):
    problem = f"{n1} {operation} {n2}"
    return eval(problem)

num1 = int(input("What is the first number?: "))

for operation in operations:
    print(operation)

num2 = int(input("What is the second number?: "))
operation_symbol = input("Pick an operation from the choices above: ")

answer = (calculate(num1, num2, operation_symbol))
print(f'{num1} {operation_symbol} {num2} = {answer}')