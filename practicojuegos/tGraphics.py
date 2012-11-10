import tBall
import tWall
import tMath
import math
import random

w1 = tWall.tWall(tMath.Vector(1, 0), tMath.Vector(1, 500),
                 color="red", tag="w1")
w2 = tWall.tWall(tMath.Vector(100, 0), tMath.Vector(100, 500),
                 color="red", tag="w2")
w3 = tWall.tWall(tMath.Vector(200, 0), tMath.Vector(200, 500),
                 color="red", tag="w3")
w4 = tWall.tWall(tMath.Vector(300, 0), tMath.Vector(300, 500),
                 color="red", tag="w4")
w5 = tWall.tWall(tMath.Vector(400, 0), tMath.Vector(400, 500),
                 color="red", tag="w5")
w6 = tWall.tWall(tMath.Vector(500, 0), tMath.Vector(500, 500),
                 color="red", tag="w6")
h1 = tWall.tWall(tMath.Vector(0, 0), tMath.Vector(500, 0),
                 color="magenta", tag="h1")
h2 = tWall.tWall(tMath.Vector(0, 100), tMath.Vector(500, 100),
                 color="magenta", tag="h2")
h3 = tWall.tWall(tMath.Vector(0, 200), tMath.Vector(500, 200),
                 color="magenta", tag="h3")
h4 = tWall.tWall(tMath.Vector(0, 300), tMath.Vector(500, 300),
                 color="magenta", tag="h4")
h5 = tWall.tWall(tMath.Vector(0, 400), tMath.Vector(500, 400),
                 color="magenta", tag="h5")
h6 = tWall.tWall(tMath.Vector(0, 500), tMath.Vector(500, 500),
                 color="magenta", tag="h6")
b1 = tBall.tBall(5, tMath.Vector(100,100), color="yellow", tag="b1")
b2 = tBall.tBall(7, tMath.Vector(150,200), color="yellow", tag="b2")

dynamicObjects = [b1, b2]
for i in range(10):
    dynamicObjects.append(tBall.tBall(3,
        tMath.Vector(random.randint(0,500),random.randint(0,500)),
        color="white", tag="ba"+str(i)))

class Level(object):
    def __init__(self):
        self.loX, self.loY, self.hiX, self.hiY = 0,0,500,500

level = Level()

def initialize(canvas):
    staticObjects = [w1, w2, w3, w4, w5, w6, h1, h2, h3, h4, h5, h6]
    pts = []
##    for i in range(4):
##        pt = tMath.Vector(random.randint(0,500),random.randint(0,500))
##        print(pt, abs(pt))
##        pts.append(pt)
##    staticObjects.extend([tWall.tWall(pts[0], pts[1]),
##                          tWall.tWall(pts[2], pts[3])])
##    intersect = tMath.intersection(pts[0], pts[1], pts[2], pts[3])
##    if intersect:
##        staticObjects.append(tBall.tBall(10,intersect, color="green", tag="i"))
    for ob in staticObjects:
        ob.paint(canvas)
##    for angle in range(0,360,5):
##        alpha = angle*math.pi/180.0
##        b=tBall.tBall(10, tMath.rotate( tMath.Vector(100,100),
##                                  tMath.Vector(150,100),
##                                  alpha),
##                      color = "red")
##        b.paint(canvas)
    
     
def myPaint(canvas):
   for ob in dynamicObjects:
        canvas.delete(ob.tag)
        print(ob)
        ob.update(level, dynamicObjects)
        ob.paint(canvas)
   canvas.update()
        
    
    
