# wap to find the largest and smallest no in a lists

a = [12, 4, 33, 23, 54]

small = a[0]
large = a[0]
for i in range(5):
    if a[i] < small:
        small = a[i]
    else:
        if a[i] > large:
            large = a[i]
print("smallest element in list is "+str(small))
print("largest element in list is "+str(large))
