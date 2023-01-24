#! /usr/bin/python3

# translate user enter data into words

data = {1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero"
        }

sum = 0
r = 0
n = int(input("enter number: "))
while (n > 0):
        r = n % 10
        sum = (sum*10) + r
        n //= 10

while (sum > 0):
        r = sum % 10
        print(data[r], end=" ")
        sum //= 10
print()
