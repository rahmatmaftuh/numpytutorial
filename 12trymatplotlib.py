import numpy as np 
import matplotlib.pyplot as plt 

#persamaan garis y = 3x+5

x = np.arange(0,11,0.5)
y = 3*x+5
print(x)
print(y)

plt.plot(x,y)
plt.show()
