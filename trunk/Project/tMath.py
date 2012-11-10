import math

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({:6.2f},{:6.2f})".format(float(self.x), float(self.y))
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    def __abs__(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    def __rmul__(self, nr):
        return Vector(nr*self.x, nr*self.y)
    def normalize(self, newLength):
        d = math.sqrt(self.x*self.x + self.y*self.y)
        return Vector(newLength*self.x/d, newLength*self.y/d)

class Matrix(object):
    def __init__(self, a11, a12, a21, a22):
        self.c11 = a11
        self.c12 = a12
        self.c21 = a21
        self.c22 = a22
    def __str__(self):
        return "({},{})({}{})".format(self.c11, self.c12, self.c21, self.c22)
    def __add__(self, other):
        return Matrix(self.c11+other.c11, self.c12+other.c12, self.c21+other.c21,
                      self.c22+other.c22)
    def __mul__(self, other):
        return Vector(self.c11*other.x + self.c12*other.y,
                      self.c21*other.x + self.c22*other.y)

def rotate(pt, pivot, alpha):
    return Vector(0,0)

def intersection(a, b, c, d):
    return None

   



    
