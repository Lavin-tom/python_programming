#! /usr/bin/python3

# sum of two nos using modules concept

#import sum                 # importing full file
from sum import sum         # import specific fun only

x, y = input("enter nos : ").split(' ')
x = int(x)
y = int(y)

result = sum.sum(x, y)
print(result)
