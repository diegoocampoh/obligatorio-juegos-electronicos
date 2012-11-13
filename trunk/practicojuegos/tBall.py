from movingObject import *
from tMath import *
import random

class tBall(movingObject):
    def __init__(self, size, location, color="yellow", tag=None):
        movingObject.__init__(self, location, Vector(random.randint(1,5),
                              random.randint(1,5)), tag=tag)
        self.size = size
        self.color = color
    
    def paint(self, canvas):
        xc, yc = int(self.location.x), int(self.location.y)
        offset = int(self.size/2)
        canvas.create_oval(xc-offset, yc-offset, xc+offset, yc+offset,
                           fill=self.color, tags=self.tag)
         
    def changeMaxVelocity(self,newValue):
        self.maxVelocity = newValue
        
        
