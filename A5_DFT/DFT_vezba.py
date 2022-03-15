import numpy as np
import matplotlib.pyplot as plt
import cmath
from scipy.fft import fft, ifft

N=64 # dolzina na niza
n=np.asarray(list(range(0,N)))
Omega= (2.0*np.pi / 64)*2
Fi=np.pi/6
x=np.zeros(N)
for i in range (N):
 #   x[i]=np.cos(Omega*i*Fi)
    x[i]=2*np.cos(Omega*i*Fi)+np.sin(Omega*3*i)+np.cos(Omega*5*i+np.pi/3)

    print(x)
    plt.figure()
    plt.stem(n,x,use_line_collection=True)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title("Izgled na singlaot")
    plt.show()


