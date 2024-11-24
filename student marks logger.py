from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import os

def clear_list():
    display.delete(0,END)
    marks.clear()

def clear_boxes():
    name_entry.delete(0,END)
    rollNumber_entry.delete(0,END)
    scienceMarks_entry.delete(0,END)
    mathsMarks_entry.delete(0,END)
    percentage_entry.delete(0,END)

def display_marks(event):
    details_window = Toplevel(root)
    name = display.get(display.curselection())
    details_text = "NAME: "+name
    details_list= marks[name]
    details_text += "\nROLL NUMBER: "+details_list[0]
    details_text += "\nSCIENCE MARKS: "+details_list[1]
    details_text += "\nMATHS MARKS: "+details_list[2]
    details_text += "\nPERCENTAGE: "+details_list[3]
    details_label = Label(details_window,text=details_text)
    details_label.pack()
    clear_boxes()

def update_add():
    name = name_entry.get()
    if name.strip() == "":
        messagebox.showerror("no name","enter a name")
    else:
        if name not in marks:
            display.insert(END,name)
        marks[name] = [rollNumber_entry.get(),scienceMarks_entry.get(),mathsMarks_entry.get(),percentage_entry.get()]

def edit():
    clear_boxes()
    index = display.curselection()
    if index:
        name = display.get(index)
        name_entry.insert(0,name)
        details = marks.get(name)
        rollNumber_entry.insert(0,details[0])
        scienceMarks_entry.insert(0,details[1])
        mathsMarks_entry.insert(0,details[2])
        percentage_entry.insert(0,details[3])
    else:
        messagebox.showerror("no index","select a name")

def delete():
    index = display.curselection()
    if index:
        del marks[display.get(index)]
        display.delete(index)
        print(display.get(index))
        print(marks)
        clear_boxes()
    else:
        messagebox.showerror("no index","select a name")

def open():
    global marks
    clear_list()
    input_file = askopenfile()
    if input_file:
        marks = eval(input_file.read())
        for key in marks:
            display.insert(END,key)
        title_label.config(text=os.path.basename(input_file.name))
    else:
        messagebox.showerror("file not selected","file not selected")

def save():
    user_file = asksaveasfile(defaultextension="*.txt")
    if user_file:
        print(marks,file=user_file)
        clear_boxes()
    else:
        messagebox.showerror("save failed","file not saved")

marks = {}

root = Tk()
root.title("student marks logger")

title_label = Label(root,text="student marks logger")
title_label.grid(row=0,column=0,pady=10,padx=10)

name_label = Label(root,text="Name: ")
name_label.grid(row=1,column=0,padx=10,pady=10)
name_entry = Entry(root)
name_entry.grid(row=1,column=1,padx=10,pady=10)

rollNumber_label = Label(root,text="Roll Number: ")
rollNumber_label.grid(row=2,column=0,padx=10,pady=10)
rollNumber_entry = Entry(root)
rollNumber_entry.grid(row=2,column=1,padx=10,pady=10)

scienceMarks_label = Label(root,text="Science Marks: ")
scienceMarks_label.grid(row=1,column=3,padx=10,pady=10)
scienceMarks_entry = Entry(root)
scienceMarks_entry.grid(row=1,column=4,padx=10,pady=10)

mathsMarks_label = Label(root,text="Maths Marks: ")
mathsMarks_label.grid(row=2,column=3,padx=10,pady=10)
mathsMarks_entry = Entry(root)
mathsMarks_entry.grid(row=2,column=4,padx=10,pady=10)

percentage_label = Label(root,text="Percentage: ")
percentage_label.grid(row=3,column=3,padx=10,pady=10)
percentage_entry = Entry(root)
percentage_entry.grid(row=3,column=4,padx=10,pady=10)

display = Listbox(root)
display.grid(row=4,column=0,columnspan=5,padx=10,pady=10)
display.bind("<<ListboxSelect>>",display_marks)

edit_btn = Button(root,text="edit",command=edit)
edit_btn.grid(row=5,column=0,padx=10,pady=10)
del_btn = Button(root,text="delete",command=delete)
del_btn.grid(row=5,column=1,padx=10,pady=10)
open_btn = Button(root,text="open",command=open)
open_btn.grid(row=5,column=2,padx=10,pady=10)
updateAdd_btn = Button(root,text="Update / Add",command=update_add)
updateAdd_btn.grid(row=5,column=3,padx=10,pady=10)
save_btn = Button(root,text="save",command=save)
save_btn.grid(row=5,column=4,padx=10,pady=10)

root.mainloop()
