# return index where values are even
import numpy as np
arr = np.array([1,2,3,4,5,6])
x = np.where(arr%2==0)
print(x)