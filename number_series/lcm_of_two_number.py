#! /usr/bin/python3

# wap to find the LCM of two numbers

def lcm(a, b):
    if a > b:
        if a % b == 0:
            print(a)
        else:
            print(a*b)
    elif b > a:
        if b % a == 0:
            print(b)
        else:
            print(a*b)
    else:
        print(a*b)


a, b = input("enter two numbers: ").split()
lcm(int(a), int(b))
