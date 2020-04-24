# Basic Calculator using Tkinter

from tkinter import *
import math as m
from math import sin, tan, cos, sqrt
import tkinter.font as font


# key in box

e = Entry(root, width=35, borderwidth=50,
          bg='#000000', foreground='white', font=32)
e.grid(row=0, columnspan=5, padx=10, pady=50)


def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():

    e.delete(0, END)


# operation

def button_add():

    first_number = e.get()

    global f_num
    global m
    m = "addition"

    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():

    first_number = e.get()

    global f_num
    global m
    m = "subtraction"

    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():

    first_number = e.get()

    global f_num
    global m
    m = "multiplication"

    f_num = int(first_number)
    e.delete(0, END)


def button_divide():

    first_number = e.get()

    global f_num
    global m
    m = "division"

    f_num = int(first_number)
    e.delete(0, END)


def button_equal():

    second_number = e.get()
    e.delete(0, END)

    if m == "addition":

        e.insert(0, f_num + int(second_number))

    if m == "subtraction":

        e.insert(0, f_num - int(second_number))

    if m == "multiplication":

        e.insert(0, f_num * int(second_number))

    if m == "division":

        e.insert(0, f_num / int(second_number))


def button_sqrt():

    first_number = e.get()

    global f_num
    global m
    m = "sqrt"

    f_num = int(first_number)
    e.insert(0, sqrt(f_num))


def button_sin():

    first_number = e.get()

    global f_num
    global m
    m = "sin"

    f_num = int(first_number)
    pi = 3.14159265359
    rad = pi / 180
    e.insert(0, sin(f_num*rad))


def button_tan():

    first_number = e.get()

    global f_num
    global m
    m = "tan"

    f_num = int(first_number)
    pi = 3.14159265359
    rad = pi / 180
    e.insert(0, tan(f_num*rad))


def button_cos():

    first_number = e.get()

    global f_num
    global m
    m = "cos"

    f_num = int(first_number)
    pi = 3.14159265359
    rad = pi / 180
    e.insert(0, cos(f_num*rad))


# define buttons

button_1 = Button(root, text="1", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg='#000000', fg="white", font='20',
                  command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, bg='#000000', fg="white", font='20',
                    command=button_add)
button_subtract = Button(root, text="-", padx=42, pady=20, bg='#000000', fg="white", font='20',
                         command=button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, bg='#000000', fg="white", font='20',
                         command=button_multiply)
button_divide = Button(root, text="/", padx=42, pady=20, bg='#000000', fg="white", font='20',
                       command=button_divide)
button_sqrt = Button(root, text=" √ ", padx=36, pady=20, bg='#141414', fg="white", font='20',
                     command=button_sqrt)

button_sin = Button(root, text="sin", padx=34, pady=20, bg='#141414', fg="white", font='20',
                    command=button_sin)
button_tan = Button(root, text="tan", padx=34, pady=20, bg='#141414', fg="white", font='20',
                    command=button_tan)
button_cos = Button(root, text="cos", padx=32, pady=20, bg='#141414', fg="white", font='20',
                    command=button_cos)

button_equal = Button(root, text="=", padx=40, pady=20, bg='#c41212', fg="white", font='20',
                      command=button_equal)
button_clear = Button(root, text="clr", padx=36, bg='#c41212', fg="white", font='20',
                      pady=20, command=button_clear)


# put buttons on screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)
button_clear.grid(row=5, column=0)
button_equal.grid(row=5, column=2)

button_sin.grid(row=1, column=0)
button_tan.grid(row=1, column=1)
button_cos.grid(row=1, column=2)

button_sqrt.grid(row=1, column=4)
button_add.grid(row=2, column=4)
button_subtract.grid(row=3, column=4)
button_multiply.grid(row=4, column=4)
button_divide.grid(row=5, column=4)


# print

root = Tk()
root.title("Calculator")
root.iconbitmap('calculator.ico')
root.mainloop()
