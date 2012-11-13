from tBall import *

class tFarmer(tBall):
    def __init__(self, location):
        tBall.__init__(self, 30, location, "yellow", "farmer")
        self.velocity = Vector(0,0)
        self.maxAcceleration = 5
        self.maxVelocity = 5
    
    def getAcceleration(self, level, dynamicObjects, staticObjects,diccionario):
        #avoid leaving box
        return self.acceleration
        