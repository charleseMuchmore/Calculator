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
window.geometry('233x282')

# text_box = Entry(window).pack()
# text_box.configure(width=20, bg='snow', fg='gray40', font=("Times", "50"))

entry_box = Entry(window)
entry_box.configure(width=11, bg='snow', fg='gray40', font=("Times", "30"))
entry_box.place(x = 4, y = 0)

btn1 = Button(window, text="1", font=("Times", "10"), command=set_text('1')).place(height = 60, width = 60, x = 0, y = 49)
btn2 = Button(window, text="2", font=("Times", "10"), command=set_text("2")).place(height = 60, width = 60, x = 58, y = 49)
btn3 = Button(window, text="3", font=("Times", "10"), command=set_text("3")).place(height = 60, width = 60, x = 116, y = 49)
btn4 = Button(window, text="4", font=("Times", "10"), command=set_text("4")).place(height = 60, width = 60, x =0, y = 107)
btn5 = Button(window, text="5", font=("Times", "10"), command=set_text("5")).place(height = 60, width = 60, x =58, y = 107)
btn6 = Button(window, text="6", font=("Times", "10"), command=set_text("6")).place(height = 60, width = 60, x =116, y = 107)
btn7 = Button(window, text="7", font=("Times", "10"), command=set_text("7")).place(height = 60, width = 60, x =0, y = 165)
btn8 = Button(window, text="8", font=("Times", "10"), command=set_text("8")).place(height = 60, width = 60, x =58, y = 165)
btn9 = Button(window, text="9", font=("Times", "10"), command=set_text("9")).place(height = 60, width = 60, x =116, y = 165)
btn0 = Button(window, text='0', font=("Times", "10"), command=set_text("0")).place(height = 60, width = 60, x = 0, y = 223)
add_btn = Button(window, text = '+', font=("Times", "10"), command=set_text("")).place(height = 60, width = 60, x = 174, y = 49)
subtract_btn = Button(window, text = '-', font=("Times", "10"), command=set_text("")).place(height = 60, width = 60, x = 174, y = 107)
multiply_btn = Button(window, text = '*', font=("Times", "10"), command=set_text("")).place(height = 60, width = 60, x = 174, y = 165)
enter_btn = Button(window, text='Enter', font=("Times", "10"), command=set_text("")).place(height = 60, width = 118, x = 58, y = 223)
divide_btn = Button(window, text = '/', font=("Times", "10"), command=set_text("")).place(height = 60, width = 60, x = 174, y = 223)


window.mainloop()