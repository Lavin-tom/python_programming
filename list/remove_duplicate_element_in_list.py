#! /usr/bin/python3

# remove duplicate element from a list

a = [1, 2, 2, 3, 4, 4, 5]
b = []
for i in a:
    if i not in b:
        b.append(i)

print(b)
