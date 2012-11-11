from tBall import *

class tSheep(tBall):
    def __init__(self, location, tag = ""):
        tBall.__init__(self, 10, location, "white", "sheep" + tag)
        self.maxAcceleration = 2
        self.maxVelocity = 2
        self.velocity = Vector(2,2)
        self.isDead = False
    
    def getAcceleration(self, level, dynamicObjects):
        #avoid leaving box
        if self.isDead:
            self.color = "red"
            self.velocity = Vector(0,0)
            return Vector(0,0)
        else:
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
            farmer = dynamicObjects[0]
            if acc.x == 0 and acc.y == 0:
                if distancePointToPoint(farmer.location, self.location) <= 100:
                    acc += self.location - farmer.location
            return acc
        