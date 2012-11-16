from tBall import *
from Tkinter import *
import Tkinter

class tFarmer(tBall):
    def __init__(self, location):
        tBall.__init__(self, 30, location, "yellow", "farmer")
        self.velocity = Vector(0,0)
        self.maxAcceleration = 5
        self.maxVelocity = 5
        
#    def update(self, level, dynamicObjects,staticObjects, diccionario):
#        tBall.update(self, level, dynamicObjects, staticObjects, diccionario)
#        speed = abs(self.velocity) 
#        if self.location.x <= level.loX+5*speed or self.location.y <= level.loY+5*speed or self.location.x >= level.hiX-5*speed or self.location.y >= level.hiY-5*speed:
#            self.location -= self.velocity
#            self.velocity = Vector(0,0) 
#    
#    def getAcceleration(self, level, dynamicObjects, staticObjects,diccionario):
#        #avoid leaving box
#        return self.acceleration
    def paint(self, canvas):
        xc, yc = int(self.location.x), int(self.location.y)
        self.image = PhotoImage(file="c:/guardian.gif")    
        self.imageId= canvas.create_image(xc, yc,anchor=Tkinter.CENTER , image=self.image)