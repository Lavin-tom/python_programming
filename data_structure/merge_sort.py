#! /usr/bin/python3

def merge(arr, left, middle, r):

    n1 = (middle - left)+1
    n2 = r - middle
    L = []
    M = []
    for i in range(0, n1):
        L.append(arr[left + i])

    for j in range(0, n2):
        M.append(arr[middle + 1 + j])

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= M[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = M[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = M[j]
        j += 1
        k += 1


def mergeSort(arr, left, r):
    if left < r:
        middle = (left + (r-1))//2
        mergeSort(arr, left, middle)
        mergeSort(arr, middle+1, r)
        merge(arr, left, middle, r)


arr = [12, 32, 6, 13, 23, 8]

mergeSort(arr, 0, len(arr)-1)
print(arr)
