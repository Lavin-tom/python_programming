# NumPy - ndim
# ndim - used to find the dimention of the array
import numpy as np
a = np.array(1)
b = np.array([1,2])
c = np.array([[1,2],[1,2]])
d = np.array([[[1,2],[1,2]],[[1,2],[1,2]]])
e = np.array([1,2,3,4],ndmin=5)

print(e)
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)