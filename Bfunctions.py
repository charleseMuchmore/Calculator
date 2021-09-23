from os import system, name
from Afunctions import *

def clear():
    """Clears the terminal"""
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def ask_for_input(cont):
    """Asks the user for a first number, an operation, and a second number, returns a dictionary with those three items as values"""
    the_dict = {}
    if cont == 'n':
        first_num = float(input("First num: "))
        the_dict["first_num"] = first_num
    print_ops()
    operation = input("Operation: ")
    if operation == '':
        while operation == '':
            operation = print("An operation is needed: ")
            the_dict["operation"] = operation
    else:
        the_dict["operation"] = operation
    second_num = float(input("Second num: "))
    the_dict["second_num"] = second_num
    return the_dict

def give_input(num, dict_input, param1):
    # """takes a first number (num), a dictionary with the operation and second number, and"""
    # dict_input = ask_for_input()
    first_num = num
    operation = dict_input["operation"]
    second_num = dict_input["second_num"]
    answer = calculate(dict_input[param1], dict_input["second_num"], dict_input["operation"])
    print(f"{first_num} {operation} {second_num} = {answer}")
    return answer
# def require_input(string):
#     if string == '':
#         while string == '':
#             return input("An input is needed")

