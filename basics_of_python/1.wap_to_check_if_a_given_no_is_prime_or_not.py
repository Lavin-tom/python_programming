# wap to check the given no is prime or not


n = int(input("Enter the no: "))
count = 0
m = int(n/2)
for i in range(1, m):
    if n % i == 0:
        count += 1
if (count == 1):
    print(str(n) + " is a prime no")
else:
    print(str(n) + " is not prime no")
