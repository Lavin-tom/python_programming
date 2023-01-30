#! /usr/bin/python3
# wap to find the length of no

n = int(input("enter any no: "))
length = 0
while n > 0:
    length += 1
    n //= 10

print(length)
