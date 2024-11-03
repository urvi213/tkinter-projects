from tkinter import *
from tkinter import messagebox

def change():
    colour = colours_listbox.curselection()
    if colour:
        try: root.configure(bg=colours_listbox.get(colour))
        except: messagebox.showerror("error","invalid")

def add():
    colours_listbox.insert(END,entry.get())

def delete():
    colour = colours_listbox.curselection()
    if colour:
        for item in colour:
            colours_listbox.delete(item)

root = Tk()

entry = Entry(root)
entry.grid(row=0,padx=40,pady=10)
add_btn = Button(root,text="ADD",command=add)
add_btn.grid(row=1,padx=40,pady=10)
delete_btn  =Button(root,text="DELETE",command=delete)
delete_btn.grid(row=2,padx=40,pady=10)
colours_listbox = Listbox(root)
colours_listbox.grid(row=3,padx=40,pady=10) 
change_btn = Button(root,text="CHANGE COLOUR",command=change)
change_btn.grid(row=4,padx=40,pady=10)

colours_listbox.insert(0,"red")
colours_listbox.insert(1,"orange")
colours_listbox.insert(2,"magenta")

root.mainloop()