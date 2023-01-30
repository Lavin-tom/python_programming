#! /usr/bin/python3


# date format
# convert date format 12/1/1997 -> 1997112

date = input("enter date in format of dd/mm/yyyy: ")
num = 0
array = []
length = len(date)
for i in range(length):
    if date[i] != '/':
        num = num * 10 + int(date[i])
    if date[i] == '/' or i == length -1:
        array.append(num)
        num = 0

for i in range(2, -1, -1):
    print(array[i], end="")
print()
