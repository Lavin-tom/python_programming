#! /usr/bin/python3

# is the input , factorial of a integer or not

flag = 0


def isFactorial(a):
    fact = 1
    global flag
    for i in range(1, a):
        fact = fact * i
        if (fact == a):
            flag = 1
            print(flag)
            break


a = int(input("enter n: "))
isFactorial(a)
if flag == 1:
    print(True)
else:
    print(False)
