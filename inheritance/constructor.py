# inheritace
# basics of inheritance

class A:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class B:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


obj_base = A("John Honai", 38)
obj_derived = B("Edger Lui", 22)

obj_base.display()
obj_derived.display()
