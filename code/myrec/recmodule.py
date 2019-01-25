class Rectangle(object):
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h
        
    def area(self):
        return self.w * self.h
    
    def __str__(self):
        return f'Rectangle w:{self.w}, h:{self.h}, area:{self.area()}'

class Square(Rectangle):
    def __init__(self, w=0):
        self.w = w
        self.h = w