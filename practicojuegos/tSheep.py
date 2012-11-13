from tBall import *
from Tkinter import *

class tSheep(tBall):
    def __init__(self, location, tag = ""):
        tBall.__init__(self, 10, location, "white", "sheep" + tag)
        self.maxAcceleration = 2
        self.maxVelocity = 2
        self.velocity = Vector(2,2)
        self.isDead = False
        self.aliveImage = None
        self.aliveImageId = None
        self.deadImage = None
        self.deadImageId = None
        self.isInCorral = False
   
    
    def getAcceleration(self, level, dynamicObjects,staticObjects,diccionario):
        
        corralx = diccionario['limiteXCorral']
        corraly = diccionario['limiteYCorral']
        
        #avoid leaving box
        if self.isDead:
            self.color = "red"
            self.velocity = Vector(0,0)
            return Vector(0,0)
        else:
            acc = Vector(0,0) 
            speed = abs(self.velocity)
            
            
            if ((self.location.x < corralx) and
                (self.location.y < corraly) and not self.isInCorral) :
                self.isInCorral = True
            
            if self.isInCorral :
                if self.location.x < level.loX+5*speed:
                    acc += Vector(self.maxAcceleration,0)
                if self.location.y < level.loY+5*speed:
                    acc += Vector(0,self.maxAcceleration)
                if self.location.x > corralx-5*speed:
                    acc += Vector(-self.maxAcceleration,0)
                if self.location.y > corraly-5*speed:
                    acc += Vector(0,-self.maxAcceleration)
            else: 
                if self.location.x < level.loX+5*speed:
                    acc += Vector(self.maxAcceleration,0)
                if self.location.y < level.loY+5*speed:
                    acc += Vector(0,self.maxAcceleration)
                if self.location.x > level.hiX-5*speed:
                    acc += Vector(-self.maxAcceleration,0)
                if self.location.y > level.hiY-5*speed:
                    acc += Vector(0,-self.maxAcceleration)
            farmer = dynamicObjects[0]
            wolf = dynamicObjects[1]
            if acc.x == 0 and acc.y == 0:
                if distancePointToPoint(farmer.location, self.location) <= 100:
                    acc += self.location - farmer.location
                if distancePointToPoint(wolf.location, self.location) <=100:
                    acc += self.location - wolf.location
            return acc
        
    def paint(self, canvas):
            xc, yc = int(self.location.x), int(self.location.y)
            offset = int(self.size/2)            
            self.aliveImage = PhotoImage(file="c:/aliveSheep.gif")
            self.deadImage = PhotoImage(file="c:/deadSheep.gif")            
            if (not self.isDead):
                self.aliveImageId = canvas.create_image(xc, yc, image=self.aliveImage)
            else:
                self.deadImageId = canvas.create_image(xc, yc, image=self.deadImage)
 
        