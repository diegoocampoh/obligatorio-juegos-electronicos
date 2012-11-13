from tBall import *
from Tkinter import *
import Tkinter
import sys

class tWolf(tBall):
    def __init__(self, location):
        tBall.__init__(self, 20, location, "brown", "wolf")
        self.maxAcceleration = 5
        self.maxVelocity = 5
        self.velocity = Vector(3,3)
    
    def getAcceleration(self, level, dynamicObjects, staticObjects,diccionario):
        #avoid leaving box
        acc = Vector(0,0) 
        speed = abs(self.velocity)
        if self.location.x < level.loX+5*speed:
            acc += Vector(self.maxAcceleration,0)
        if self.location.y < level.loY+5*speed:
            acc += Vector(0,self.maxAcceleration)
        if self.location.x > level.hiX-5*speed:
            acc += Vector(-self.maxAcceleration,0)
        if self.location.y > level.hiY-5*speed:
            acc += Vector(0,-self.maxAcceleration)
        bestDistance = sys.maxint
        bestTarget = None
        farmer = dynamicObjects[0]
        corral = diccionario['corral']
        # si no tengo que esquivar muros
        if acc.x == 0 and acc.y == 0:
            # escapa del granjero y de la puerta del corral
            if(distancePointToPoint(self.location, corral.centro)<=corral.radioProteccion):
                acc += self.location - corral.centro
            
            if (distancePointToPoint(self.location, farmer.location) <= 100):
                acc += self.location - farmer.location
            else:
                # ataca ovejas
                for ob in dynamicObjects:
                    if "sheep" in ob.tag :
                        if not ob.isDead and not ob.isInCorral:
                            distance = distancePointToPoint(self.location, ob.location)
                            if distance <=10:
                                ob.isDead = True
                            else:
                                if distance < bestDistance:
                                    bestTarget = ob
                if bestTarget != None:
                    acc += bestTarget.location - self.location
        return acc
    
    def paint(self, canvas):
        xc, yc = int(self.location.x), int(self.location.y)
                  
        self.image = PhotoImage(file="c:/wolfAnim.gif")    
        self.imageId= canvas.create_image(xc, yc, anchor=Tkinter.CENTER ,image=self.image)

    
           
        