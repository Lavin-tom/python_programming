#! /usr/bin/python3


# insertion sort
def insertionSort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


arr = [123, 434, 343, 233, 211]

print(arr)

insertionSort(arr)
print(arr)
