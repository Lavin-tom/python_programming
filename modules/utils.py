#! /usr/bin/python3

# defenision to find the largest element from a list
def find_max(a):
    maximum = a[0]
    for i in a:
        if i > maximum:
            maximum = i
    return maximum


def add_element(a):
    n = int(input("enter list size: "))
    print("enter elements: ")
    for i in range(0, n):
        a.append(int(input()))
    return a
