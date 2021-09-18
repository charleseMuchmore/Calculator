from tkinter import *
import tkinter as tk

def set_text(num):
    # entry_box.delete(0, END)
    entry_box.insert(END, num)

# def set_text1(num):
#     entry_box.insert(END, num)


window = Tk()
window.title("Simple Calculator")
window.configure(background="azure")
window.geometry('305x400')

# text_box = Entry(window).pack()
# text_box.configure(width=20, bg='snow', fg='gray40', font=("Times", "50"))

entry_box = Entry(window)
entry_box.pack()
entry_box.configure(width=15, bg='snow', fg='gray40', font=("Times", "30"))

btn0 = Button(window, text='0', font=("Times", "10"), command=set_text("0")).pack(ipadx = 10, ipady = 5)
btn1 = Button(window, text="1", font=("Times", "10"), command=set_text('1')).pack(ipadx = 10, ipady = 5)
btn2 = Button(window, text="2", font=("Times", "10"), command=set_text("2")).pack(ipadx = 10, ipady = 5)
btn3 = Button(window, text="3", font=("Times", "10"), command=set_text("3")).pack(ipadx = 10, ipady = 5)
btn4 = Button(window, text="4", font=("Times", "10"), command=set_text("4")).pack(ipadx = 10, ipady = 5)
btn5 = Button(window, text="5", font=("Times", "10"), command=set_text("5")).pack(ipadx = 10, ipady = 5)
btn6 = Button(window, text="6", font=("Times", "10"), command=set_text("6")).pack(ipadx = 10, ipady = 5)
btn7 = Button(window, text="7", font=("Times", "10"), command=set_text("7")).pack(ipadx = 10, ipady = 5)
btn8 = Button(window, text="8", font=("Times", "10"), command=set_text("8")).pack(ipadx = 10, ipady = 5)
btn9 = Button(window, text="9", font=("Times", "10"), command=set_text("9")).pack(ipadx = 10, ipady = 5)

window.mainloop()