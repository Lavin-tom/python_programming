#! /usr/bin/python3

a = [1, 2, 3, 4, 5]

a.append(10)            # add element at the end of the list
print(a)
a.insert(0, 20)         # insert element to a exact postion
print(a)

print(50 in a)          # check 50 is available in list a
print(5 in a)           # return True

a.sort()                # to sort the list in accending order
print(a)

a.reverse()             # to reverse the list
print(a)

b = a.copy()            # to copy one list to another
print(b)
