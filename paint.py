from tkinter import *

class Paint(object):
    START_PEN = 5
    START_COLOUR = "black"

    def __init__(self):
        print("e")
        self.root = Tk()
        self.pen_btn = Button(self.root,text="pen")
        self.pen_btn.grid(row=0,column=0,padx=10,pady=5)
        self.brush_btn = Button(self.root,text="brush")
        self.brush_btn.grid(row=0,column=1,padx=10,pady=5)
        self.colour_btn = Button(self.root,text="colour")
        self.colour_btn.grid(row=0,column=2,padx=10,pady=5)
        self.eraser_btn = Button(self.root,text="eraser")
        self.eraser_btn.grid(row=0,column=3,padx=10,pady=5)
        self.scale = Scale(self.root,from_=1,to=15,orient=HORIZONTAL)
        self.scale.grid(row=0,column=4,padx=10,pady=5)
        self.canvas = Canvas(self.root,width=400,height=400,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=5,padx=10,pady=5)

        self.root.mainloop()
        print("e")
        self.setup()

    def setup(self):
        self.oldx=None
        self.oldy=None
        self.colour = self.START_COLOUR
        self.width = self.START_PEN
        self.is_eraser = False
        self.active_button = self.pen_btn


paint = Paint()
