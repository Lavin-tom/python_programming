#decorators basics
#decorators - we want to modify a function logic without modifing actual fuction

def decorCircle(func):
    def inner(r):
        if r > 100:
            r = 100
        return func(r)
    return inner

@decorCircle
def circle(r):
    area = 3.14*r*r
    return area

#circle = decorCircle(circle)   #either we can create like this or using @we can add
print(circle(100))              #these @ method is only work if our actual fuction is with us
print(circle(200))      #for radius above 100, reset to 100 
print(circle(95))