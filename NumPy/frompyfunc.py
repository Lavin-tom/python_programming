# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.
import numpy as np

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1)

print(myadd([1,2,3,4],[5,6,7,8]))