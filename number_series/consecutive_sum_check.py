#! /usr/bin/python3

# consecutive sum check

def consecutiveSum(a):
    for i in range(1, a):
        sum = 0
        for j in range(i, a):
            sum = sum + j
            if sum == a:
                for k in range(i, j+1):
                    print(k, end="")
                    if k != j:
                        print(' + ', end='')
                print()


a = int(input("enter no : "))
consecutiveSum(a)
