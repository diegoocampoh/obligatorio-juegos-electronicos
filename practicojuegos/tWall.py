import random

class tWall(object):
    def __init__(self, pta, ptb, color="white",
                 tag = None):
        self.x1, self.x2, self.y1, self.y2 = pta.x, ptb.x, pta.y, ptb.y
        self.color = color
        self.tag = tag
    
    def paint(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           fill=self.color, tags= self.tag)
