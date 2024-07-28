from tkinter import *
import tkinter.font as font

def convert():
    dollar_output = entry_box.get()
    if dollar_output.replace(".","",1).isdigit(): #replace(removed part, replacement, amount of times)
        dollar_output = int(dollar_output)*1.29
        output_label.config(text=str(dollar_output))
        error_label.config(text="")
    else:
        output_label.config(text="")
        error_label.config(text="invalid input")

root = Tk()
root.configure(background="white")
root.title("currency converter")

frame1 = Frame(root)
frame1.pack(padx=30,pady=30)

title_label = Label(frame1,text="convert £ to $",font=font.Font(size=30))
title_label.grid(row=0,column=1)

entry_label = Label(frame1,text="amount in £:",font=font.Font(size=15))
entry_label.grid(row=2,column=0)
entry_box = Entry(frame1)
entry_box.grid(row=2,column=2)

output_title_label = Label(frame1,text="amount in $:",font=font.Font(size=15))
output_title_label.grid(row=3,column=0)
output_label = Label(frame1)
output_label.grid(row=3,column=2)

convert_btn = Button(frame1,text="convert",background="pink",font=font.Font(size=30),command=convert)
convert_btn.grid(row=4,column=1)

error_label = Label(frame1,text="",fg="red",font=font.Font(size=15))
error_label.grid(row=5,column=1)

root.mainloop()