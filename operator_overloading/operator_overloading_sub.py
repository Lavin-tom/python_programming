#! /usr/bin/python3

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __sub__(self, other):
        obj = Point(0, 0)

        obj.x = self.x - other.x
        obj.y = self.y - other.y

        return obj


p1 = Point(6, 5)
p2 = Point(3, 4)
p3 = p1 - p2
print(p3.x, p3.y)
