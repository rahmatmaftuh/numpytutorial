import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

#stacking matrix = susunan matrix
c = np.hstack((a,b)) #susunan secara horizontal
d = np.vstack((a,b)) #susunan secara vertical
print(c)