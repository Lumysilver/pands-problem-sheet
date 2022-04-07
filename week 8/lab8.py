#messing with matplotlib


import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoint = xpoints * xpoints 

plt.plot(xpoints, ypoint)
plt.show()

