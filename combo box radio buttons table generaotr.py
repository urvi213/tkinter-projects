from tkinter import *
from tkinter.ttk import * # this is the module we get combobox from

root = Tk()
root.title("table generator")

title_label = Label(root,text="Table Generator")
title_label.grid(column=0,columnspan=3,row=0)

options_label = Label(root,text="Number and Range:")
options_label.grid(column=0,columnspan=1,row=1,padx=10,pady=5)

number_combo_box = Combobox(root,values=list(range(50)),width=20)
number_combo_box.grid(column=1,columnspan=1,row=1,padx=10,pady=5)

root.mainloop()