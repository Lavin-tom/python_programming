#wap to check year is leap year or not

def checkLeapYear(year):
    if (((year%4 ==0) and (year%100!=0)) or (year%400==0)):
        return True


if checkLeapYear(2000):
    print("Leap year")
else:
    print("Not leap year")