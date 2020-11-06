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
import math
window= tk.Tk()
window.title("tk")
window.geometry("320x160")
win=window

state1 = IntVar()
state1.set(0)
state2 = IntVar()
state2.set(0)
state3 = IntVar()
state3.set(0)
state4 = IntVar()
state4.set(0)
state5 = IntVar()
state5.set(0)
state6 = IntVar()
state6.set(0)
state7 = IntVar()
state7.set(0)
state8 = IntVar()
state8.set(0)




#------------------------------------------


def binary_to_decimal(binary):
    
    if binary[0]==1:
        a=128
    else:
        a=0
    
    if binary[1]==1:
        b=64
    else:
        b=0

    if binary[2]==1:
        c=32
    else:
        c=0

    if binary[3]==1:
        d=16
    else:
        d=0

    if binary[4]==1:
        e=8
    else:
        e=0

    if binary[5]==1:
        f=4
    else:
        f=0

    if binary[6]==1:
        g=2
    else:
        g=0

    if binary[7]==1:
        h=1
    else:
        h=0

    decimal= a+b+c+d+e+f+g+h
    return decimal
    get_binary()

    # binary is a tuple of length 8
    # return value is an integer decimal
    

    #return decimal 

def decimal_to_binary(m1):
    binary2=[]


    n1= m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)

    n1 = m1%2
    m1 = m1//2
    binary2.append(n1)


  #     o1= (n1 % 2)
  #     o1= int(o1)
  #     binary2.append(o1)
  # else:
  #     binary2.append(0)
  # if n1 > 1:
  #     p1= n1/2
  #     q1= (p1 % 2)
  #     q1= int(q1)
  #     binary2.append(q1)
  # if p1 > 1:
  #     r1= p1/2
  #     s1= (r1 % 2)
  #     s1= int(s1)
  #     binary2.append(s1)
  # if r1 > 1:
  #     t1= r1/2
  #     u1= (t1 % 2)
  #     u1= int(u1)
  #     binary2.append(u1)
  # if t1 > 1:
  #     v1= t1/2
  #     w1= (v1 % 2)
  #     w1= int(w1)
  #     binary2.append(w1)
  # if v1 > 1:
  #     y1= v1/2
  #     z1= (y1 % 2)
  #     z1= int(z1)
  #     binary2.append(z1)


   # if r > 1:
    #   decimal_to_binary(r//2)
    #s= (r % 2)

    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    return binary2
    get_binary()
    #return binary


def get_binary():

    m1= e1.get()
    m1= int(m1)


    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes

    binary2 = decimal_to_binary(m1)

    if binary2[7]==1:
        state1.set(1)
    else:
        state1.set(0)

    if binary2[6]==1:
        state2.set(1)
    else:
        state2.set(0)

    if binary2[5]==1:
        state3.set(1)
    else:
        state3.set(0)

    if binary2[4]==1:
       state4.set(1)
    else:
       state4.set(0)

    if binary2[3]==1:
       state5.set(1)
    else:
       state5.set(0)

    if binary2[2]==1:
       state6.set(1)
    else:
       state6.set(0)

    if binary2[1]==1:
       state7.set(1)
    else:
       state7.set(0)

    if binary2[0]==1:
       state8.set(1)
    else:
       state8.set(0)



    e1.delete(0,tk.END)
    e1.insert(0, state1.get())
    e1.delete(1,tk.END)
    e1.insert(1, state2.get())
    e1.delete(2,tk.END)
    e1.insert(2, state3.get())
    e1.delete(3,tk.END)
    e1.insert(3, state4.get())
    e1.delete(4,tk.END)
    e1.insert(4, state5.get())
    e1.delete(5,tk.END)
    e1.insert(5, state6.get())  
    e1.delete(6,tk.END)
    e1.insert(6, state7.get())
    e1.delete(7,tk.END)
    e1.insert(7, state8.get())
    

    




def get_decimal():
    c1 = IntVar()
    c1 = c1.get()
    c2 = IntVar()
    c2 = c2.get()
    c3 = IntVar()
    c3 = c3.get()
    c4 = IntVar()
    c4 = c4.get()
    c5 = IntVar()
    c5 = c5.get()
    c6 = IntVar()
    c6 = c6.get()
    c7 = IntVar()
    c7 = c7.get()
    c8 = IntVar()
    c8 = c8.get()

    e1.delete(0,tk.END)
    e1.insert(0, state1.get())
    e1.delete(1,tk.END)
    e1.insert(1, state2.get())
    e1.delete(2,tk.END)
    e1.insert(2, state3.get())
    e1.delete(3,tk.END)
    e1.insert(3, state4.get())
    e1.delete(4,tk.END)
    e1.insert(4, state5.get())
    e1.delete(5,tk.END)
    e1.insert(5, state6.get())  
    e1.delete(6,tk.END)
    e1.insert(6, state7.get())
    e1.delete(7,tk.END)
    e1.insert(7, state8.get())





    binary = []
    binary.append(state1.get())
    binary.append(state2.get())
    binary.append(state3.get())
    binary.append(state4.get())
    binary.append(state5.get())
    binary.append(state6.get())
    binary.append(state7.get())
    binary.append(state8.get())


    binary_to_decimal(binary)


    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box

    decimal = binary_to_decimal(binary)

    e1.delete(0, tk.END)
    e1.delete(1, tk.END)
    e1.delete(2, tk.END)
    e1.delete(3, tk.END)
    e1.delete(4, tk.END)
    e1.delete(5, tk.END)
    e1.delete(6, tk.END)
    e1.delete(7, tk.END)

    e1.insert(0, decimal)
    #takes return from binary to decimal



e1 = Entry(win)
e1.insert(0,state1.get())
#--------------------------------------

l1 = Label(win, text="Binary / Decimal Converter!")
c1 = Checkbutton(win, variable = state1, command=get_decimal())
c2 = Checkbutton(win, variable = state2, command=get_decimal())
c3 = Checkbutton(win, variable = state3, command=get_decimal())
c4 = Checkbutton(win, variable = state4, command=get_decimal())
c5 = Checkbutton(win, variable = state5, command=get_decimal())
c6 = Checkbutton(win, variable = state6, command=get_decimal())
c7 = Checkbutton(win, variable = state7, command=get_decimal())
c8 = Checkbutton(win, variable = state8, command=get_decimal())

b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)
e1 = Entry(win, text="1")

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

#Next day to do

#Decimal to binary, the 101010 in printed
#1
#0
#1
#0
#1
#0

#Need to fix that into a tuple to then turn boxes and have binary on entry widget.