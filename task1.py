#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *
window= tk.Tk()
window.title("tk")
window.geometry("320x150")
win=window

#------------------------------------------


def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    pass

    #return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    pass
    #return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    pass
    binary = binary_to_decimal(decimal)


def get_decimal():
    binary = []
    a=1
    binary.append(a)

    e1.delete(0,tk.END)
    e1.insert(0, state.get())


    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    decimal = binary_to_decimal(binary)




state = IntVar()
state.set(1)
#--------------------------------------

l1 = Label(win, text="Binary / Decimal Converter!")
c1 = Checkbutton(win, variable = state, command=get_decimal())
c2 = Checkbutton(win, variable = state, command=get_decimal())
c3 = Checkbutton(win, variable = state, command=get_decimal())
c4 = Checkbutton(win, variable = state, command=get_decimal())
c5 = Checkbutton(win, variable = state, command=get_decimal())
c6 = Checkbutton(win, variable = state, command=get_decimal())
c7 = Checkbutton(win, variable = state, command=get_decimal())
c8 = Checkbutton(win, variable = state, command=get_decimal())

b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)
e1 = Entry(win)

#-------------------------------------
l1.pack()
c1.place(x= 10, y= 50)
c2.place(x= 50, y= 50)
c3.place(x= 90, y=50)
c4.place(x=130, y=50)
c5.place(x=170, y=50)
c6.place(x=210, y=50)
c7.place(x=250, y=50)
c8.place(x=290, y=50)
b1.place(x=50, y=100)
b2.place(x=160, y=100)
e1.place(x=100, y=130)



#--------------------------------------
win.mainloop()