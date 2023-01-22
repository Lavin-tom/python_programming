# function over riding
# deriving same function in base clas and derived class , if  we call function with derived class object 
# it shows derived class fuction only 
# to get base class function result we use super()

class base:
    def display(self):
        print("testing of base class")


class derived(base):
    def display(self):
        print("testing of derived class")
        super().display()


obj_derived = derived()
obj_derived.display()
