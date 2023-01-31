#! /usr/bin/python3

# wap to print the prime nos in a range

def primeInRange(a, b):
    for i in range(a, b+1):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count == 1:
            print(i, end=" ")
    print()


a, b = input("enter range of prime no you want : ").split()

primeInRange(int(a), int(b))
