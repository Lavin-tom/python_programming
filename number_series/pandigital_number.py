#! /usr/bin/python3

# wap to check the no is pandigital or not
# pandigital means no that contain zero to nine atleast ones

def isPandigital(a):
    count = 0
    for j in range(0, 10):
        for i in a:
            if j == int(i):
                count += 1
                break
    if count == 10:
        return True
    else:
        return False


a = input("enter nos: ")
print(isPandigital(a))
