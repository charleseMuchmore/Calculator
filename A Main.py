# from tkinter import *
# import tkinter as tk
from Functions import *

first_num = int(input("First num: "))
print(" + \n - \n * \n /")
operation = input("Operation: ")
second_num = int(input("Second num: "))

if operation == '':
    print("An operation is needed")
elif operation == '+':
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