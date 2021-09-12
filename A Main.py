# from tkinter import *
# import tkinter as tk
from Functions import *

dict_input = ask_for_input()
first_num = dict_input["first_num"]
operation = dict_input["operation"]
second_num = dict_input["second_num"]

answer = calculate(first_num, second_num, operation)
print(f"{first_num} {operation} {second_num} = {answer}")

# cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation")
# if cont == 'y':

   

# print(ask_for_input())
