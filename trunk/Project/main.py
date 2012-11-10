from tkinter import *
from tGraphics import *

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
        self.startButton.grid(row=0, column=0)
        self.stopButton.grid(row=0, column=1)
        self.quitButton.grid(row=0, column=2)
        initialize(self.canvas)
    
    def runAnimation(self):
        while(self.animate):
            myPaint(self.canvas)
            self.canvas.after(frameTime)
    def displayAnimation(self):
        myPaint(self.canvas)

        

root = Tk()
root.title("Thomas Schwarz: AI, hw1")
cw = 1000
ch = 1000
frameTime=100 #milliseconds between frame updates

app = Application(master=root)
app.mainloop()
#root.destroy()

