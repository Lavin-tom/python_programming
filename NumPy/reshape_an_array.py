# reshape an array
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,0])
# put -1 when we don't know the size, numpy auto calculate the value
new_arr = arr.reshape(2,-1)

print(arr)
print(arr.shape)
print(new_arr)
print(new_arr.shape)