# wap to print first n prime nos
n = int(input("enter n : "))
count = 0
r = 0
for j in range(2, 100):
    count = 0
    for i in range(2, int((j/2)+1)):
        if j % i == 0:
            count += 1
    if count == 0:
        print(j, end=" ")
        r += 1
    if (r == n):
        break
