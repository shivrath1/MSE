
class Rectangle:
    def __init__(self, length, width) :
        self.length = length
        self.width = width

    def cal_area(self) :
        return self.length * self.width
    
    def cal_perimeter(self) :
        return 2*(self.length + self.width)