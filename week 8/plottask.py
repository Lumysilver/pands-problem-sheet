#Write a program called plottask.py that displays a plot of the functions
#  f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#I have started by import numpy as np, but wasn't found and I'll follow the steps 
#and trying to install Numpy
#after few tries to install Numpy, I had to uninstall Anaconda and reinstall again Python


# import numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

## initialize  empty list for f g and h to store the Y points
fpoints = []
gpoints = []
hpoints = []

# define functions to calculate f, g and x Y points
def f(x):
    return x

def g(x):
    return x**2

def h(x):
    return x**3

# use while to loop from 0 to 4 and calculate for each value the f, g and h Y points
# and append/populate them to the f, g h lists
i = 0
while i < 5:
    fpoints.append(f(i))
    gpoints.append(g(i))
    hpoints.append(h(i))
    i += 1

# build the X and Y axes for f, g and h
#we use defaut x points https://www.w3schools.com/python/matplotlib_plotting.asp
yfpoints = np.array(fpoints)
ygpoints = np.array(gpoints)
yhpoints = np.array(hpoints)

# plot
#mark each point with a red circle: https://www.w3schools.com/python/matplotlib_markers.asp
plt.plot(yfpoints, 'o:r')

#mark each point with a green circle
plt.plot(ygpoints, 'o:g')

#mark each point with a blue circle
plt.plot(yhpoints, 'o:b')


# output the plot
plt.show()
