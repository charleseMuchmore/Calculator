from os import system, name

def clear():
    """Clears the terminal"""
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def add(num1, num2):
    """Adds"""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies"""
    return num1 * num2

def divide(num1, num2):
    """Divides"""
    return num1 / num2