# wap print the Fibonacci series up to a given number of terms

n = int(input("enter n "))
f = 0
s = 1
print(f, s, end=" ")
for i in range(0, (n-2)):
    sum = f + s
    print(str(sum), end=" ")
    f = s
    s = sum
