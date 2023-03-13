# transpose of matrix without temp matrix
# not completed 

def set_array(arr,r,c):
    print("enter array elements: ")
    for i in range(0,r):
        for j in range(0,c):
            #n = input("enter array elements")
            arr[i][j] = input("")


def get_array(arr,r,c):
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end=" ")
    print("\n")


def transposeArray(arr,r,c):
    for i in range(r):
        for j in range(i,c):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

arr =[]
r,c = input("enter array size\n").split()
r = int(r)
c = int(c)
set_array(arr,r,c)
get_array(arr,r,c)
#transposeArray(arr,r,c)
get_array(arr,r,c)
