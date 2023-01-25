#! /usr/bin/python3
# operator overloading - greater than

class Point:
    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        obj = Point(0)
        obj.x = self.x > other.x
        return obj


p1 = Point(14)
p2 = Point(2)
p3 = p1 > p2
print(p3.x)
