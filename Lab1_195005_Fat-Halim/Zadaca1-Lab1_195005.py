import math

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,1000)
x=[-1,2,-3,0,2,3,-1,5,2,2]
plt.plot(t, np.sin((0.7 *math.pi*t)+0.4))
plt.show()

