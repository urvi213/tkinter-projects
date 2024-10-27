from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

def add():
    file_list.insert(END,entry.get()) # end is a constant
    entry.delete(0,END) # takes (start,end)

def delete_item():
    selection = file_list.curselection() # function returns list of indexes selected items
    if selection:
        #file_list.delete(selection) # function takes index of items to delete
        for item in selection:
            file_list.delete(item)

def save():
    user_file = asksaveasfile(defaultextension="*.txt")
    print(user_file)
    if user_file != None:
        for item in file_list.get(0,END):
            print(item.strip(),file=user_file) # print is writing onto the file

def open():
    input_file = askopenfile()
    if input_file != None:
        file_list.delete(0,END)
        for line in input_file:
            file_list.insert(END,line)

root = Tk()

save_btn = Button(root,text="SAVE",command=save)
save_btn.grid(row=0,column=1,padx=10,pady=10)

entry = Entry(root)
entry.grid(row=1,column=1,padx=10,pady=10)

add_btn = Button(root,text="ADD",command=add)
add_btn.grid(row=2,column=1,padx=10,pady=10)

open_btn = Button(root,text="OPEN",command=open)
open_btn.grid(row=3,column=0,padx=10,pady=10)

file_list = Listbox(root,selectmode="multiple") # default listbox lets you select one at a time
for i in range(10):
    file_list.insert(i,"LIST {}".format(i+1))
file_list.grid(row=3,column=1,padx=10,pady=10)

del_btn = Button(root,text="DELETE",command=delete_item)
del_btn.grid(row=3,column=2,padx=10,pady=10)

root.mainloop()