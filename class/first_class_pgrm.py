# first class implementation

class A:

    def display(self):
        print("inside the class A")


class B:

    def display(self):
        print("inside the class B")


obj_a = A()
obj_b = B()

obj_a.display()
obj_b.display()
