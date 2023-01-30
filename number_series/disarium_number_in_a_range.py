#! /usr/bin/python3

# wap to check the no is disarium no or not
# print disarium no in a range

m, n = input("enter start and stop range : ").split()
print(f"disarium no between {m} and {n} is :")
for j in range(int(m), int(n)):
    num = j
    length = 0
    nos = 0
    while num > 0:
        length += 1
        num //= 10

    num = j
    while num > 0:
        r = num % 10
        nos = nos + (r ** length)
        length -= 1
        num //= 10

    if j == nos:
        print(j, end=" ")
print()
