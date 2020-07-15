class Rectangle:
    def __init__(self,length,width):
        self.leng=length
        self.wid=width
    def area(self):
        return self.leng*self.wid

class Circle:
    def __init__(self,radius):
        self.rad=radius
    def area(self):
        return math.pi*(self.rad**2)
