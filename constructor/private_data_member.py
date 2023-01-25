#! /usr/bin/python3
# __ (mangling) is used to set that variable as private, it actually not encapsulate the data
# still it can access inside the class and main as a normal variable 
# it used to represent for identify the developer to use that variable carefull and not use as a public

class Point:
    def __init__(self):
        self.__data = "private data"

    def get_data(self):
        print(self.__data)

    def set_data(self, value):
        self.__data = value


obj = Point()
obj.__data          # create error
obj.set_data("new data")
obj.get_data
