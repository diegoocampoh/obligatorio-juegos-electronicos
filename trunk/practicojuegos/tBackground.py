import random
from Tkinter import *

class tBackground(object):
    def __init__(self, imagefile):
        self.imageFile = imagefile
        self.image = None
        self.imageId = None
    
    def paint(self, canvas):
        self.image = PhotoImage(file=self.imageFile)
        self.imageId =  canvas.create_image(0, 0, anchor=NW, image=self.image, tags="fondo")
