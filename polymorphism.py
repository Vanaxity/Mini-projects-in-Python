from abc import ABC, abstractmethod


class shape:
    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2

class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 1/2*self.base*self.height

shapes = [circle(4), square(5), triangle(12,6)]
for shape in shapes:
    print(shape.area())
