#! /usr/bin/python3

class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(self.x,self.y)


class Child:
    pass

parent = Parent(100, 200)
parent.display()
