#! /usr/bin/python3

# exception handling
try:
    age = int(input("enter age: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age should not be zero")
