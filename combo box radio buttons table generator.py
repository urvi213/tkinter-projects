from tkinter import *
from tkinter.ttk import * # this is the module we get combobox from

def generate():
    table_var= ""
    multiplier_var = multiplier.get()
    for i in range(1,table_range.get()+1):
        table_var += "\n{} * {} = {}".format(multiplier_var,i,multiplier_var*i)
    #print(table_var)
    table_label.config(text=table_var)

root = Tk()
root.title("table generator")

multiplier = IntVar()
table_range = IntVar() # sets its value based on which is pressed out of a set of radio buttons and what their value is
table_range.set(10)

title_label = Label(root,text="Table Generator")
title_label.grid(column=0,columnspan=3,row=0)

options_label = Label(root,text="Number and Range:")
options_label.grid(column=0,columnspan=1,row=1,padx=10,pady=5)

number_combo_box = Combobox(root,values=list(range(50)),width=20,textvariable=multiplier)
number_combo_box.grid(column=1,columnspan=1,row=1,padx=10,pady=5)

ten_btn = Radiobutton(root,text=10,value=10,variable=table_range)
ten_btn.grid(column=2,row=1,padx=10,pady=5)

twenty_btn = Radiobutton(root,text=20,value=20,variable=table_range)
twenty_btn.grid(column=2,row=2,padx=10,pady=5)

thirty_btn = Radiobutton(root,text=30,value=30,variable=table_range)
thirty_btn.grid(column=2,row=3,padx=10,pady=5)

generate_btn = Button(root,text="generate",command=generate)
generate_btn.grid(row=3,column=1,padx=10,pady=5)

table_label = Label(root)
table_label.grid(row=4,column=0,columnspan=3,padx=10,pady=5)

root.mainloop()