#! /usr/bin/python3

# decorators
def find_area(r):
    pi = 3.14
    area = 2 * pi * r**2
    return area


def circle_decor(fun):
    def inner(r):
        if r > 100:
            r = 100
        return fun(r)
    return inner


fa = circle_decor(find_area)
print(fa(120))
