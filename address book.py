from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox

address_book = {}

def clear_boxes():
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    email_entry.delete(0,END)
    mobile_entry.delete(0,END)
    birthday_entry.delete(0,END)

def display(event):
    details_window = Toplevel(root)
    name = book_display.get(book_display.curselection())
    details_text = "NAME: "+name
    details_list= address_book[name]
    details_text += "\nADDRESS: "+details_list[0]
    details_text += "\nEMAIL: "+details_list[1]
    details_text += "\nMOBILE: "+details_list[2]
    details_text += "\nBIRTHDAY: "+details_list[3]
    details_label = Label(details_window,text=details_text)
    details_label.pack()
    clear_boxes()

def update_add():
    name = name_entry.get()
    if name.strip() == "":
        messagebox.showerror("no name","enter a name")
    else:
        if name not in address_book:
            book_display.insert(END,name)
        address_book[name] = [address_entry.get(),email_entry.get(),mobile_entry.get(),birthday_entry.get()]

root = Tk()
root.title("address book :3")

title_label = Label(root,text="My Address Book")
title_label.grid(row=0,column=1,padx=5,pady=5)
open_btn = Button(root,text="Open")
open_btn.grid(row=0,column=2,padx=5,pady=5)

book_display = Listbox(root) # bind
book_display.bind("<<ListboxSelect>>",display)
book_display.grid(row=1,column=0,rowspan=5,columnspan=2,padx=5,pady=5)

name_label = Label(root,text="Name: ")
name_label.grid(row=1,column=2)
name_entry = Entry(root)
name_entry.grid(row=1,column=3,padx=5)

address_label = Label(root,text="Adress: ")
address_label.grid(row=2,column=2)
address_entry = Entry(root)
address_entry.grid(row=2,column=3,padx=5)

mobile_label = Label(root,text="Mobile: ")
mobile_label.grid(row=3,column=2)
mobile_entry = Entry(root)
mobile_entry.grid(row=3,column=3,padx=5)

email_label = Label(root,text="Email: ")
email_label.grid(row=4,column=2)
email_entry = Entry(root)
email_entry.grid(row=4,column=3,padx=5)

birthday_label = Label(root,text="Birthday: ")
birthday_label.grid(row=5,column=2)
birthday_entry = Entry(root)
birthday_entry.grid(row=5,column=3,padx=5)

edit_btn = Button(root,text="Edit")
edit_btn.grid(row=6,column=0,padx=5,pady=5)

del_btn = Button(root,text="Delete")
del_btn.grid(row=6,column=1,padx=5,pady=5)

updateAdd_btn = Button(root,text="Update/Add",command=update_add)
updateAdd_btn.grid(row=6,column=2,columnspan=2,padx=5,pady=5)

save_btn = Button(root,text="Save")
save_btn.grid(row=7,column=0,columnspan=4,padx=5,pady=5)


root.mainloop()
