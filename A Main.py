# from tkinter import *
# import tkinter as tk
from Functions import *

first_num = float(input("First num: "))
print(" + \n - \n * \n /")
operation = input("Operation: ")

if operation == '':
    while operation == '':
        operation = print("An operation is needed: ")
        
second_num = float(input("Second num: "))

if operation == '+':
    answer = add(first_num, second_num)
elif operation == '-':
    answer = subtract(first_num, second_num)
elif operation == '*':
    answer = multiply(first_num, second_num)
elif operation == '/':
    answer = divide(first_num, second_num)
else:
    print("An invalid operation has been given")

print(f"{first_num} {operation} {second_num} = {answer}")