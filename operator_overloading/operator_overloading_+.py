# operator overloading +

class A:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return A(x, y)


obj1 = A(1, 2)
obj2 = A(2, 3)

print(obj1 + obj2)
