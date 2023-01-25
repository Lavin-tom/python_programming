#! /usr/bin/python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __truediv__(self, other):
        obj = Point(0, 0)
        obj.x = self.x / other.x
        obj.y = self.y / other.y
        return obj


p1 = Point(14, 25)
p2 = Point(2, 5)
p3 = p1 / p2
print(p3.x, p3.y)
