#!/usr/bin/python

from tkinter import *
from tkinter import ttk
from turtle import color
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Checkbutton(frm, text="Hello").grid(column=0, row=2)
root.mainloop()