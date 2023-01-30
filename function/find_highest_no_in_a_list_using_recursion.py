#! /usr/bin/python3

def find_highest(a, max, i):
    if i < len(a):
        if max < a[i]:
            max = a[i]
        i += 1
        find_highest(a, max, i)
    else:
        print(max)


a = [12, 232, 323, 232, 2123]
max = 0
i = 0
find_highest(a, max, i)
