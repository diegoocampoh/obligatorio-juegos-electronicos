
class tCorral(object):
    def __init__(self, centro, radioProteccion):
        self.centro = centro
        self.radioProteccion = radioProteccion
        
    def paint(self, canvas):
        xc, yc = int(self.centro.x), int(self.centro.y)
        offset = int(self.radioProteccion)
        canvas.create_oval(xc-offset, yc-offset, xc+offset, yc+offset,
                           fill='blue', tags='corral')