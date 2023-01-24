#! /usr/bin/python3

# how to find the duplicate element from a list

a = [12, 23, 23, 2, 5, 53]
a.sort()
print(a)

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count > 1:
        print(a[i])
        break
