#! /usr/bin/python3

# broken keyboard
# Given what is supposed to be typed and what is actually typed, 
# write a function that returns the broken key(s). The function looks like:

# findBrokenKeys(correct phrase, what you actually typed)

array1 = []


def findBrokenKeys(a, b):
    global array1
    for i, j in zip(a, b):
        if i != j and i not in array1:
            array1.append(i)

    print(array1)


a, b = input("enter correct and wrong phrase : ").split()

findBrokenKeys(a, b)
