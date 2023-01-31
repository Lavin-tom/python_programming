#! /usr/bin/python3
# Create a function that takes a number as an argument and returns n 
# instances of the Fibonacci sequence as an array.


def fibSeq(n, f, s):
    if n > 0:
        array.append(f)
    if n > 1:
        array.append(s)
    for i in range(0, n-2):
        sum = f + s
        array.append(sum)
        f = s
        s = sum


f = 0
s = 1
n = int(input("enter n: "))
array = []

fibSeq(n, f, s)
print(array)
