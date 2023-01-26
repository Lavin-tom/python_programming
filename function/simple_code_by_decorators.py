#! /usr/bin/python3


def my_decorator(func):
    def inner():
        print("before function call")
        func()
        print("after function call")
    return inner


@my_decorator
def my_function():
    print("inside my_function")


my_function()
