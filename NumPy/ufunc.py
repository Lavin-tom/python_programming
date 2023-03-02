# ufunc- universal functions
import numpy as np
x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = []

for i,j in zip(x,y):
    z.append(i+j)

print(z)
# same as for loop addition
z = np.add(x,y)
print(z)