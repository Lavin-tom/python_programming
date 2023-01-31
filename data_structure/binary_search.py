#! /usr/bin/python3

# binary search

def binarySearch(array):
    low = 0
    r = len(array)-1
    flag = 0
    while (low <= r):
        middle = (low+r)//2

        if array[middle] == data:
            flag = 1
            return middle
        elif array[middle] > data:
            r = middle - 1
        else:
            low = middle + 1
    if flag == 0:
        return -1


data = int(input("enter data to search in array: "))
array = [12, 22, 32, 42, 52]

res = binarySearch(array)
if res != -1:
    print(f'{data} is found at index {res}')
else:
    print(f'{data} is not found in the list')
