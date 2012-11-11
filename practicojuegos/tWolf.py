from tBall import *
import sys

class tWolf(tBall):
    def __init__(self, location):
        tBall.__init__(self, 20, location, "brown", "wolf")
        self.maxAcceleration = 5
        self.maxVelocity = 5
        self.velocity = Vector(3,3)
    
    def getAcceleration(self, level, dynamicObjects):
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
        # si no tengo que esquivar muros
        if acc.x == 0 and acc.y == 0:
            # escapa del granjero
            if distancePointToPoint(self.location, farmer.location) <= 100:
                acc += self.location - farmer.location
            else:
                # ataca ovejas
                for ob in dynamicObjects:
                    if "sheep" in ob.tag :
                        if not ob.isDead:
                            distance = distancePointToPoint(self.location, ob.location)
                            if distance <=10:
                                ob.isDead = True
                            else:
                                if distance < bestDistance:
                                    bestTarget = ob
                if bestTarget != None:
                    acc += bestTarget.location - self.location
        return acc
        