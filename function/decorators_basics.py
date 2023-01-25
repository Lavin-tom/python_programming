#! /usr/bin/python3

def upper_decor(fun):
    def wrapper():
        result = fun()
        return result.upper()
    return wrapper


@upper_decor
def hello_name():
    return "hello"


print(hello_name())
