#! /usr/bin/python3


# selection sort

def selectionSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [12, 43, 6, 53, 8, 17]

print(arr)
selectionSort(arr)
print(arr)
