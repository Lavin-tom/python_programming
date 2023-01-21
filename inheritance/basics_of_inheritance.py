# inheritace
# basics of inheritance

class parent:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)


class child (parent):
    def __init__(self, value, child_value):
        super().__init__(value)
        self.child_value = child_value

    def display_child_value(self):
        print(self.child_value)


# calling using parent object
obj1 = parent(33)
obj1.display_value()

obj = child(10, 20)
obj.display_value()
obj.display_child_value()
