import tkinter as Tk

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label = Label(font=("ds-digital",80),background="slategrey",foreground="pink")
label.pack(anchor="center")
time()

mainloop()

