# wap to reverse a number

n = int(input("enter n to reverse: "))
sum=0
while(n>0):
    r = n % 10
    sum = sum*10 + r
    n=n//10

print(sum)
