# visibility of variables in a class
a = 30
class A:
    a = 10

    def display(self):
        print("inside A class")
        print("value of A: ", A.a)          #first method to access a variable declared outside the function
        print("value of A: ", self.a)       #second method to access a variable declared outside the function
        print("value of a from global: ", a)


class B:
    a = 20

    def display(self):
        print("inside B class")
        print("value of A: ", B.a)
        print("value of A: ", self.a)
        print("value of A in class A: ",A.a)        #accessing a value from class A
        print("value of a from global: ", a)


obj_a = A()
obj_b = B()

obj_a.display()
obj_b.display()
