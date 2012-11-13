import tBall
import tWall
import tMath
import tFarmer
import tSheep
import tBackground
import tWolf
import tCorral
from tMath import *
import random

#muro corral del sur
w2 = tWall.tWall(tMath.Vector(0, 192), tMath.Vector(160, 192),
                 color="red", tag="w2")
w21 = tWall.tWall(tMath.Vector(160, 192), tMath.Vector(160, 224),
                 color="red", tag="w21")
w22 = tWall.tWall(tMath.Vector(160, 224), tMath.Vector(0, 224),
                 color="red", tag="w22")

#muro corral del este
w3 = tWall.tWall(tMath.Vector(192, 0), tMath.Vector(192, 160),
                 color="red", tag="w3")
w31 = tWall.tWall(tMath.Vector(192, 160), tMath.Vector(224, 160),
                 color="red", tag="w31")
w32 = tWall.tWall(tMath.Vector(224, 160), tMath.Vector(224, 0),
                 color="red", tag="w32")

          
#Limites del mapa
w1 = tWall.tWall(tMath.Vector(1, 0), tMath.Vector(1, 640),
                 color="green", tag="w1")
w6 = tWall.tWall(tMath.Vector(640, 0), tMath.Vector(640, 640),
                 color="green", tag="w6")
h1 = tWall.tWall(tMath.Vector(0, 0), tMath.Vector(640, 0),
                 color="green", tag="h1")

h6 = tWall.tWall(tMath.Vector(0, 640), tMath.Vector(640, 640),
                 color="green", tag="h6")

#puerta corral
pc1 =tBall.tBall(5, tMath.Vector(0,0), color="blue", tag="bpc")


b1 = tBall.tBall(5, tMath.Vector(100,100), color="yellow", tag="b1")
b2 = tBall.tBall(7, tMath.Vector(150,200), color="yellow", tag="b2")
farmer = tFarmer.tFarmer(tMath.Vector(random.randint(0,640),random.randint(0,640)))
wolf = tWolf.tWolf(tMath.Vector(random.randint(300,640),random.randint(300,640)))
back = tBackground.tBackground(imagefile="c:\mapa.gif")
corral = tCorral.tCorral(tMath.Vector(0,0), 230)

dynamicObjects = [farmer, wolf]
staticObjects = [back,corral,w1,w2,w21,w22,w3,w31,w32, h1, h6,w6]

dicObjects = {'limiteXCorral': w3.x1 , 'limiteYCorral':w2.y1, 'corral':corral}

for i in range(10):
    dynamicObjects.append(tSheep.tSheep(tMath.Vector(random.randint(corral.radioProteccion,640),random.randint(corral.radioProteccion,640)), tag=str(i)))
#    dynamicObjects.append(tBall.tBall(3,
#        tMath.Vector(random.randint(0,500),random.randint(0,500)),
#        color="white", tag="ba"+str(i)))

class Level(object):
    def __init__(self):
        self.loX, self.loY, self.hiX, self.hiY = 0,0,640,640

level = Level()

def initialize(canvas):
    
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
    return dynamicObjects
    
     
def myPaint(canvas):
   for ob in dynamicObjects:
        canvas.delete(ob.tag)
        ob.update(level, dynamicObjects,staticObjects,dicObjects)
        ob.paint(canvas)
   canvas.update()
   

def key(event):
    if event.char == 'a':
        farmer.velocity = Vector(-farmer.maxVelocity,0)
    elif event.char == 's':
        farmer.velocity = Vector(0,farmer.maxVelocity)
    elif event.char == 'd':
        farmer.velocity = Vector(farmer.maxVelocity,0)
    elif event.char == 'w':
        farmer.velocity = Vector(0,-farmer.maxVelocity)
    elif event.char == 'f':
        farmer.velocity = Vector(0,0)
    print "pressed", repr(event.char)
        
    
    
