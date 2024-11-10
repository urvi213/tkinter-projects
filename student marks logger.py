from tkinter import *
from tkinter import messagebox

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

edit_btn = Button(root,text="edit")
edit_btn.grid(row=5,column=0,padx=10,pady=10)
del_btn = Button(root,text="delete")
del_btn.grid(row=5,column=1,padx=10,pady=10)
open_btn = Button(root,text="open")
open_btn.grid(row=5,column=2,padx=10,pady=10)
updateAdd_btn = Button(root,text="Update / Add",command=update_add)
updateAdd_btn.grid(row=5,column=3,padx=10,pady=10)
save_btn = Button(root,text="save")
save_btn.grid(row=5,column=4,padx=10,pady=10)

root.mainloop()