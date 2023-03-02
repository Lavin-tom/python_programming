# copy in numpy
# changes in copied array is not reflect on original array
import numpy as np
arr = np.array([1,2,3,4,5])
copy_arr = arr.copy()

copy_arr[0]=11
print(arr)
print(copy_arr)