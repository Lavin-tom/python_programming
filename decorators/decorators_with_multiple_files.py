#decorators
#here we are importing AreaCircle function from circle
#we need to modify logic of that function when radius is greather than 100, limit radius to 100
#we can acheive this through decorators
 
from circle import AreaCircle

def decorCircle(func):
    def inner(r):
        if r>100:
            r = 100
        return func(r)
    return inner

AreaCircle = decorCircle(AreaCircle)
print(AreaCircle(100))
print(AreaCircle(200))
print(AreaCircle(48))