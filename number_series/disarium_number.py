#! /usr/bin/python3

# wap to check the no is disarium no or not

n = input("enter any no: ")
length = len(n)
num = int(n)
nos = 0
j = 1
for i in n:
    nos = nos + (int(i) ** j)
    j += 1

if nos == int(n):
    print(f'{n} is a disarium no')
else:
    print(f'{n} is not a disarium no')
