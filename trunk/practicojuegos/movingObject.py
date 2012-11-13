from tMath import *
import random

class movingObject(object):
    def __init__(self, location, velocity, acceleration=Vector(0,0), tag="",
                 maxAcceleration = 3,
                 maxVelocity= 5):
        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration
        self.maxAcceleration = maxAcceleration
        self.maxVelocity = maxVelocity
        self.tag = tag
        self.changeVelocity = False
        
    def update(self, level, dynamicObjects,staticObjects, diccionario):
        self.acceleration = self.getAcceleration(level, dynamicObjects,staticObjects,diccionario)
        if abs(self.acceleration) > self.maxAcceleration:
            self.acceleration = self.acceleration.normalize(self.maxAcceleration)
        speed = abs(self.velocity)
        self.velocity += self.acceleration
        if self.changeVelocity == False:
            self.velocity = self.velocity.normalize(speed)
        elif abs(self.velocity)> self.maxVelocity:
            self.velocity = self.velocity.normalize(self.maxVelocity)
        self.location += self.velocity
    
    def getAcceleration(self, level, dynamicObjects, diccionario):
        #avoid leaving box
        self.acceleration
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
        if acc.x == 0 and acc.y== 0:
            for ob in dynamicObjects:
                if ob != self and self != dynamicObjects[0]:
                    if distancePointToPoint(ob.location, self.location) < 20:
                        acc -= ob.location - self.location
        if acc.x == 0 and acc.y== 0:
            ob = dynamicObjects[0]
            if ob != self:
                acc += ob.location - self.location
        if acc.x == 0 and acc.y== 0:
            acc += Vector(random.random()-0.5, random.random()-0.5)
        return acc

    def __repr__(self):
        return "s={}, v={}, a={}".format(self.location,
                                         self.velocity,
                                         self.acceleration)
            
        
#class steering(object):
#    @staticmethod
#    def getAcceleration(mOb, level, dynamicObjects):
#        #avoid leaving box
#        acc = Vector(0,0) 
#        speed = abs(mOb.velocity)
#        if mOb.location.x < level.loX+5*speed:
#            acc += Vector(mOb.maxAcceleration,0)
#        if mOb.location.y < level.loY+5*speed:
#            acc += Vector(0,mOb.maxAcceleration)
#        if mOb.location.x > level.hiX-5*speed:
#            acc += Vector(-mOb.maxAcceleration,0)
#        if mOb.location.y > level.hiY-5*speed:
#            acc += Vector(0,-mOb.maxAcceleration)
#        if acc.x == 0 and acc.y== 0:
#            for ob in dynamicObjects:
#                if ob != mOb and mOb != dynamicObjects[0]:
#                    if distancePointToPoint(ob.location, mOb.location) < 20:
#                        acc -= ob.location - mOb.location
#        if acc.x == 0 and acc.y== 0:
#            ob = dynamicObjects[0]
#            if ob != mOb:
#                acc += ob.location - mOb.location
#        if acc.x == 0 and acc.y== 0:
#            acc += Vector(random.random()-0.5, random.random()-0.5)
#        return acc      
        
	
