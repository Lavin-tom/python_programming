# user defined ufunc
import numpy as np

def myfun(x,y,z):
    return x-y-z

# function name, no of arguments, output array
myfun = np.frompyfunc(myfun,3,1)

print(myfun([1,2,3],[4,5,6],[7,8,9]))