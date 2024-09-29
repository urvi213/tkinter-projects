from tkinter import *
from tkinter.ttk import *

def order():
    #type.set(pizza_list.get())
    output_label.config(text="you have ordered {} {} {} pizza(s)".format(quantity_select.get(),size.get(),pizza_type.get()))

root = Tk()
root.title("pizza ordering")

size = StringVar()
size.set("s")
pizza_type= StringVar()

title_label = Label(root,text="welcome to the pizza shop :3")
title_label.grid(row=0,column=0,columnspan=3)

pizza_select_label = Label(root,text="select pizza type:")
pizza_select_label.grid(row=1,column=0)

quantity_select_label = Label(root,text="select quantity:")
quantity_select_label.grid(row=2,column=0)

#pizza_list = Listbox(root)
#pizza_list.grid(column=1,row=1)
#pizza_list.insert(1,"vegetable margherita")
#pizza_list.insert(2,"plain margherita")
#pizza_list.insert(3,"meat margherita")
#pizza_list.insert(4,"garlic")

pizzas=["vegetable margherita","plain margherita","meat margherita","garlic"]
pizza_list = OptionMenu(root,pizza_type,*pizzas)
pizza_type.set(pizzas[0])
#["vegetable margherita","plain margherita","meat margherita","garlic"]
pizza_list.grid(row=1,column=1)

quantity_select = Spinbox(root,from_=1,to=20)
quantity_select.grid(row=2,column=1)

s_btn = Radiobutton(root,text="s",value="s",variable=size)
s_btn.grid(column=2,row=1)

m_btn = Radiobutton(root,text="m",value="m",variable=size)
m_btn.grid(column=2,row=2)

l_btn = Radiobutton(root,text="l",value="l",variable=size)
l_btn.grid(column=2,row=3)

order_btn = Button(root,text="order",command=order)
order_btn.grid(column=1,row=4)

output_label = Label(text="-")
output_label.grid(row=5,column=0,columnspan=3)

root.mainloop()