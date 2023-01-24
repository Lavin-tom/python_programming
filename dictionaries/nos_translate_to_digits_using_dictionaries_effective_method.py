#! /usr/bin/python3

# translate user enter data into words

data = {"1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"
        }

numbers = input("enter number: ")
for i in numbers:
    print(data[i], end=" ")
print()
