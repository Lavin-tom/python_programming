# converting datatype 
import numpy as np
arr = np.array([1.1, 2.1, 3.1])

new_arr = arr.astype('i')
print(new_arr)
print(new_arr.dtype)

# convert to boolean
arr1 = np.array([1,0,1,3])
new_arr1 = arr1.astype(bool)
print(new_arr1)
print(new_arr1.dtype)
