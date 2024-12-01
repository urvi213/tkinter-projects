from tkinter import *
from tkinter.colorchooser import askcolor # to get the colour selecting box

class Paint(object):
    START_PEN = 5
    START_COLOUR = "black"

    def __init__(self):
        #print("e")
        self.root = Tk()
        self.pen_btn = Button(self.root,text="pen",command=self.use_pen)
        self.pen_btn.grid(row=0,column=0,padx=10,pady=5)
        self.brush_btn = Button(self.root,text="brush",command=self.use_brush)
        self.brush_btn.grid(row=0,column=1,padx=10,pady=5)
        self.colour_btn = Button(self.root,text="colour",command=self.choose_colour)
        self.colour_btn.grid(row=0,column=2,padx=10,pady=5)
        self.eraser_btn = Button(self.root,text="eraser",command=self.use_eraser)
        self.eraser_btn.grid(row=0,column=3,padx=10,pady=5)
        self.scale = Scale(self.root,from_=1,to=15,orient=HORIZONTAL)
        self.scale.grid(row=0,column=4,padx=10,pady=5)
        self.canvas = Canvas(self.root,width=400,height=400,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=5,padx=10,pady=5)

        self.setup()
        self.root.mainloop()
        #print("e")

    def setup(self):
        self.oldx=None
        self.oldy=None
        self.colour = self.START_COLOUR
        self.width = self.START_PEN
        self.is_eraser = False
        self.active_button = self.pen_btn
        self.canvas.bind("<B1-Motion>",self.paint) # needs function
        self.canvas.bind("<ButtonRelease-1>",self.reset)
        self.scale.set(self.START_PEN)
    
    def activate_btn(self,button,eraser_mode=False):
        self.active_button.configure(relief=RAISED)
        self.active_button = button
        self.active_button.configure(relief=SUNKEN)
        self.is_eraser = eraser_mode

    def use_pen(self):
        self.activate_btn(self.pen_btn)
    def use_brush(self):
        self.activate_btn(self.brush_btn)
    def use_eraser(self):
        self.activate_btn(self.eraser_btn,True)
    def choose_colour(self):
        self.activate_btn(self.colour_btn)
        self.colour = askcolor(color=self.colour)[1] # gets hex code
        print(self.colour)

    def paint(self,event):
        #print("asdasd")
        self.width = self.scale.get()
        paint_colour = "white" if self.is_eraser else self.colour
        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,width=self.width,fill=paint_colour,smooth=True,splinesteps=60,capstyle=ROUND)
        self.oldx = event.x
        self.oldy = event.y
    def reset(self,event):
        #print("skjdhfsdf")
        self.oldx= None
        self.oldy = None


paint = Paint()
