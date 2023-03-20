#oops basics
class Car:
    def __init__(self,make,model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed  = 0
    
    def accelerate(self,speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        self.speed -= speed_decrease

    def get_speed(self):
        print(self.speed)

my_car = Car('Toyota','Corolla',2015)
my_car.accelerate(10)
my_car.brake(5)
my_car.get_speed()