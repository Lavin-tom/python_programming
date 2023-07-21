#exception handling 

try:
    a = int(input("enter first no\n"))
    b = int(input("enter second no\n"))
    div = a/b
    print(div)
except:
        print("Denominator is zero, Division by zero error")
finally:
        print("end of code")