#! /usr/bin/python3

# circle and two square
# Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
# Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

# from radius we have to find the area using r*sqrt(2)
import math
r = int(input("enter radius of circle: "))

big_square_area = (2*r)**2
small_square_area = (r*(math.sqrt(2)))**2
res = big_square_area-small_square_area
print(math.ceil())
