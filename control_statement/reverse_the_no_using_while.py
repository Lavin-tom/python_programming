#! /usr/bin/python3

# reverse a no using while Loop

num = int(input("enter nuber to reverse"))
sum = 0
while (num > 0):
    r = num % 10
    sum = (sum * 10) + r
    num //= 10

print(sum)
