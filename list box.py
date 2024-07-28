from tkinter import *
root = Tk()
root.geometry("500x500")
root.configure(background="white")
root.title("list box")

label = Label(root,text="food",bg="black",fg="white")

food_list = Listbox(root, height=400,width=300,bg="grey",font="Arial",fg="white",activestyle="dotbox")
food_list.insert(0,"rice")
food_list.insert(1,"pizza")
food_list.insert(2,"banana")
food_list.insert(3,"onion")

label.pack()
food_list.pack()

root.mainloop()