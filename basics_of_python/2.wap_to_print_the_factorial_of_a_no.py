# wap to print the factorial of a no

n = int(input("enter number to find factorial : "))
b = 1
for i in range(1, (n+1)):
    b = b * i
print("factorial of "+str(n)+" is : "+str(b))
