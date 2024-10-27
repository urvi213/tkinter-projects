from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

root = Tk()
root.title("address book :3")

title_label = Label(root,text="My Address Book")
title_label.grid(row=0,column=1,padx=5,pady=5)
open_btn = Button(root,text="Open")
open_btn.grid(row=0,column=2,padx=5,pady=5)

book_display = Listbox(root)
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

updateAdd_btn = Button(root,text="Update/Add")
updateAdd_btn.grid(row=6,column=2,columnspan=2,padx=5,pady=5)

save_btn = Button(root,text="Save")
save_btn.grid(row=7,column=0,columnspan=4,padx=5,pady=5)


root.mainloop()