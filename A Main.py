# from tkinter import *
# import tkinter as tk
from Bfunctions import *
# from test_functions import *
cont = 'n'
dictio = ask_for_input(cont)
answer = give_input(dictio["first_num"], dictio, "first_num")
cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
while cont == 'n':
    clear()
    dictio = {}
    dictio = ask_for_input('n')
    answer = give_input(dictio["first_num"], dictio)
    cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
    while cont == 'y':
        dictio = ask_for_input(cont)
        dictio["answer"] = answer
        answer = give_input(answer, dictio)
        cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
while cont == 'y':
    dictio = ask_for_input(cont)
    dictio["answer"] = answer
    answer = give_input(answer, dictio)
    cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
    while cont == 'n':
        clear()
        dictio = {}
        dictio = ask_for_input('n')
        answer = give_input(dictio["first_num"])
        cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
