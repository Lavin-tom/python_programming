# wap to implement the bubble sort algorithm

temp = 0
arr = [12, 42, 2, 11, 54, 13]


def print_array():
    for i in range(6):
        print(arr[i], end=" ")


# sorting_definition
def sort_array():
    for i in range(6):
        for j in range(6-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


print_array()
print()         # for new line
sort_array()    # sorting funciton call
print_array()   # for print list function
