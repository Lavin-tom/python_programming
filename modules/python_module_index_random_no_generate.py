#! /usr/bin/python3

# python module index - random no GeneratorExit

import random
from utils import add_element

# genarate no b/w 0 and 1
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))           # generate no b/w 10 - 20

a = []
add_element(a)
print(random.choice(a))

