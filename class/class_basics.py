#! /usr/bin/python3

class FirstClass:
    def draw(self):
        print("draw")

    def move(self):
        print("move")


obj = FirstClass()
obj1 = FirstClass()
obj.draw()
obj.x = 12
obj.y = 13

obj1.move()
obj1.x = 22
obj1.y = 23

print(obj.x, obj.y)
print(obj1.x, obj1.y)
