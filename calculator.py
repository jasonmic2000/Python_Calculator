from tkinter import *
from typing import Match

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def addition():
    first_number = e.get()
    global f_add
    global math
    math = "addition"
    f_add = int(first_number)
    e.delete(0, END)

def subtraction():
    first_number = e.get()
    global f_sub
    global math
    math = "subtraction"
    f_sub = int(first_number)
    e.delete(0, END)

def multiplication():
    first_number = e.get()
    global f_mul
    global math
    math = "multiplication"
    f_mul = int(first_number)
    e.delete(0, END)

def division():
    first_number = e.get()
    global f_div
    global math
    math = "division"
    f_div = int(first_number)
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_add + int(second_number))
        
    elif math == "subtraction":
        e.insert(0, f_sub - int(second_number))
        
    elif math == "multiplication":
        e.insert(0, f_mul * int(second_number))
        
    elif math == "division":
        e.insert(0, f_div / int(second_number))
        



    

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text="+", padx=39, pady=20, command=addition)
button_subtraction = Button(root, text="-", padx=40, pady=20, command=subtraction)
button_multiplication = Button(root, text="x", padx=39, pady=20, command=multiplication)
button_division = Button(root, text="/", padx=40, pady=20, command=division)
button_equal = Button(root, text="=", padx=39, pady=20, command=equal)
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)

# Put buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_addition.grid(row=4, column=3)
button_subtraction.grid(row=3, column=3)
button_multiplication.grid(row=2, column=3)
button_division.grid(row=1, column=3)

button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)


root.mainloop()