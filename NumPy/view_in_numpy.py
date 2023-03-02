# view in numpy
# changes in copied array is reflect the actual array
import numpy as np
arr = np.array([1,2,3,4,5])
view_arr = arr.view()

view_arr[0]=11
print(arr)
print(view_arr)