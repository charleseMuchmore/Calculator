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
        first_num = request_firstnum()
        put_in_dict(the_dict, "first_num", first_num)
    print_ops()
    operation = request_operation()
    if operation == '':
        while operation == '':
            operation = print("An operation is needed: ")
            put_in_dict(the_dict, "operation", operation)
    else:
        the_dict["operation"] = operation
    second_num = request_secondnum()
    put_in_dict(the_dict, "second_num", second_num)
    return the_dict
def give_input(num, dict_input):
    """takes a first number (num), a dictionary containing the operation and second number, and"""
    first_num = float(num)
    operation = dict_input["operation"]
    second_num = dict_input["second_num"]
    answer = calculate(first_num, operation, second_num)
    print(f"{first_num} {operation} {second_num} = {answer}")
    return answer
# def require_input(string):
#     if string == '':
#         while string == '':
#             return input("An input is needed")

