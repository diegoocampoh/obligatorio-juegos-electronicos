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
        
    def update(self, level):
        self.acceleration = steering.getAcceleration(self, level)
        if abs(self.acceleration) > self.maxAcceleration:
            self.acceleration = self.acceleration.normalize(self.maxAcceleration)
        speed = abs(self.velocity)
        self.velocity += self.acceleration
        if self.changeVelocity == False:
            self.velocity = self.velocity.normalize(speed)
        elif abs(self.velocity)> self.maxVelocity:
            self.velocity = self.velocity.normalize(self.maxVelocity)
        self.location += self.velocity

    def __repr__(self):
        return "s={}, v={}, a={}".format(self.location,
                                         self.velocity,
                                         self.acceleration)
            
        
class steering(object):
    def getAcceleration(mOb, level):
        #avoid leaving box
        acc = Vector(0,0)
        speed = abs(mOb.velocity)
        if mOb.location.x < level.loX+5*speed:
            acc += Vector(mOb.maxAcceleration,0)
        if mOb.location.y < level.loY+5*speed:
            acc += Vector(0,mOb.maxAcceleration)
        if mOb.location.x > level.hiX-5*speed:
            acc += Vector(-mOb.maxAcceleration,0)
        if mOb.location.y > level.hiY-5*speed:
            acc += Vector(0,-mOb.maxAcceleration)
            
        return Vector(random.random()-0.5, random.random()-0.5) + acc      
        
	
