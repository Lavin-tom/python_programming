#! /usr/bin/python3

# constructor

class First:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def display(self):
        print(self.a, self.b)


obj = First(10, 20)
obj.display()

# we can modify the data outside the class
obj.a = 55
obj.b = 66
obj.display()
