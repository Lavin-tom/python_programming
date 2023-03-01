# super function
# inheritance the base and derived class having functions with same name 
# when we call functions using derived class object
# is showing child class function result only 
# to get the result from parent class we use super() function

class parent:
    def display(self):
        print("print from parent class")


class child(parent):
    def display(self):
        super().display()                   #get display function from parent class
        print("print from child class")


obj = child()
obj.display()
