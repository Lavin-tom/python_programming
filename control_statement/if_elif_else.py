#! /usr/bin/python3
# if elif else

a, b, c = int(input("enter a")), int(input("enter b")), int(input("enter c"))
if a < b:
    if a > c:
        print(f'{a} is large')
    else:
        print(f"{c} is large")
elif b > c:
    print(f"{b} is large")
else:
    print(f"{c} is large")
