# wap to find the common elements in two list 

a = [12, 23, 34]
b = [1, 23, 4]
for i in range(2):
    for j in range(2):
        if (a[i] == b[j]):
            print(a[i], end=" ")
