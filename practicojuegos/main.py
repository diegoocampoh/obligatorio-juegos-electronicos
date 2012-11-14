
from Tkinter import * 
from tGraphics import *
from tMath import rotate, intersection, distancePointToSegment
from tMath import Vector

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
    def animateTrue(self):
        self.animate=True
        self.runAnimation()
    def animateFalse(self):
        self.animate=False
        self.displayAnimation()  
    def createWidgets(self):
        self.startButton = Button(root, bg = "white",
                                    text="Start",
                                    fg="black",
                                    command=self.animateTrue)
        self.stopButton = Button(root, bg = "white",
                                    text="Step",
                                    fg="black",
                                    command=self.animateFalse)
        self.quitButton = Button(root, bg = "white",
                                    text="Quit",
                                    fg="black",
                                    command=self.master.destroy)
        self.canvas=Canvas(root, width=cw, height=ch, background="black")
        self.canvas.grid(row=1, column=0, columnspan=50)
        self.canvas.bind( "<Button-1>", paint )
        self.startButton.grid(row=0, column=0)
        self.stopButton.grid(row=0, column=1)
        self.quitButton.grid(row=0, column=2)
        dynamicObjects = initialize(self.canvas)
    
    def runAnimation(self):
        while(self.animate):
            myPaint(self.canvas)
            self.canvas.after(frameTime)
            
    def displayAnimation(self):
        myPaint(self.canvas)
        
    def paintPoint(self, point, color):
        x1, y1 = ( point.x - 1 ), ( point.y - 1 )
        x2, y2 = ( point.x + 1 ), ( point.y + 1 )
        self.canvas.create_oval( x1, y1, x2, y2, fill = color )
    
        
    
def paint( event ):
    python_green = "white"
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    app.canvas.create_oval( x1, y1, x2, y2, fill = python_green )

        

root = Tk()
root.title("Cuidando las ovejitas")
cw = 640
ch = 640
frameTime=50 #milliseconds between frame updates
root.bind("<Key>", key)
app = Application(master=root)
app.mainloop()
#root.destroy()

