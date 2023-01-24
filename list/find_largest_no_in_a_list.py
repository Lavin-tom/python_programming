#! /usr/bin/python3

a = [12, 32, 122, 434, 23, 28, 432]

large = a[0]
for i in a:
    if i > large:
        large = i

print(f"largest no in list is {large} ")
