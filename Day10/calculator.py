from calculator_art import *

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

def calculate(n1, n2, operation):
    problem = f"{n1} {operation} {n2}"
    return eval(problem)

print(calculate(7,3,'*'))