#! /usr/bin/python3

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        obj = Point(0, 0)

        obj.x = self.x + other.x
        obj.y = self.y + other.y

        return obj


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)
