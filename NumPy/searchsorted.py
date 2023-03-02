# searchsorted()
# equalent to binary sort, applicable only in sorted array
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)