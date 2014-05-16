import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
from pylab import *

fig=figure()
subplot(121)
x = np.linspace(-10, 10, 100)
y1 = x
y2 = x*x
y3 = x*x*x
plot(x, y1,'r')
plot(x, y2,'g')
plot(x, y3,'b')
title('normal graph')

ax = fig.add_subplot(122, polar=True)
r1 = np.arange(0,np.pi*2,0.001)
r2 = np.arange(0,2.507,0.001)
r3 = np.arange(0,1.845,0.001)
theta1 = r1
theta2 = r2*r2
theta3 = r3*r3*r3
line1 = ax.plot(theta1,r1, 'r')
line2 = ax.plot(theta2,r2, 'g')
line3 = ax.plot(theta3,r3, 'b')
title('polar graph')

plt.subplots_adjust(hspace=0.5)
plt.show()
