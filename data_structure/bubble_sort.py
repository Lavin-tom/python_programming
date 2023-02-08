#! /usr/bin/python3


# bubble sort

def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


arr = [12, 43, 6, 53, 8, 17]

print(arr)
bubbleSort(arr)
print(arr)
