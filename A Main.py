# from tkinter import *
# import tkinter as tk
from Functions import *
cont = 'n'
dictio = ask_for_input(cont)
answer = give_input(dictio["first_num"], dictio, "first_num")

cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
while cont == 'y':
    dictio = ask_for_input(cont)
    print(f"dictio first is {dictio}")
    dictio["answer"] = answer
    answer = give_input(answer, dictio, "answer")
    cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")
   
while cont == 'n':
    clear()
    dictio = ask_for_input('n')
    give_input(dictio["first_num"], dictio, dictio["first_num"])
    cont = input(f"'y' to continue calculating with {answer}, 'n' to start a new calculation: ")




#todo:
#Create a way to repeat the code as many times as the user likes
