from tMath import *
import random

class steering(object):
    @staticmethod
    def getAcceleration():
        return Vector(random.random(), random.random())
