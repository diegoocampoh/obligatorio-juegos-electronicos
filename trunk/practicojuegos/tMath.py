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
    o = pt - pivot
    rotation = Matrix(math.cos(alpha), -math.sin(alpha), math.sin(alpha), math.cos(alpha)) * o
    return rotation + pivot

def intersection(a, b, c, d):
    a1 = Vector(0,0)
    b1 = b - a
    c1 = c - a
    d1 = d - a
    distance = math.sqrt(b1.x*b1.x + b1.y*b1.y)
    cosalpha = b1.x / distance
    sinalpha = b1.y / distance
    rotationMatrix = Matrix(cosalpha, sinalpha, -sinalpha, cosalpha)
    a1 = rotationMatrix * a1
    b1 = rotationMatrix * b1
    c1 = rotationMatrix * c1
    d1 = rotationMatrix * d1
    x = (c1.y*d1.x - c1.x*d1.y) / (c1.y - d1.y)
    if x > 0 and x <b1.x:
        intersect = Vector(x, 0)
        intersect = Matrix(cosalpha, -sinalpha, sinalpha, cosalpha) * intersect + a
        return intersect
    else:
        return None
    
def distancePointToPoint(a,b):
    c = a - b 
    return math.sqrt(math.pow(c.x, 2) + math.pow(c.y, 2))
    
def distancePointToSegment(a,b,pt):
    #u = ((pt.x - a.x)(b.x - a.x) + (pt.y - a.y) + (b.y - a.y)) / (math.pow(b.x -a.x, 2) + math.pow(b.y -a.y),2)
    #if u>0 and u<1:
    return ((b.x - a.x)*(pt.y - a.y) - (b.y - a.y)*(pt.x - a.x)) / (math.sqrt(math.pow(b.x - a.x, 2) + math.pow(b.y - a.y, 2)))
    #else:
    #    return None



    
