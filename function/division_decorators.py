#! /usr/bin/python3

def super_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


@super_div
def div(a, b):
    print(a/b)


# one method
d = super_div(div)
d(2, 4)

# second method
super_div(div)(12, 24)

# third method
div(12, 36)
