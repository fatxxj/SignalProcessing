import numpy as np
import matplotlib.pyplot as plt
import cmath

N=64;
n=np.asarray(list(range(0,N)));
Omega=2.0*np.pi / 16.0
Fi=0.42

Realen=np.zeros(N);
Imaginaren = np.zeros(N);
for i in range (N):
    Realen[i]=cmath.exp(1j*(Omega*i*Fi)).real # go dava realniot del
    Imaginaren[i]=cmath.exp(1j*(Omega*i*Fi)).imag #go dava imaginarniot del
    plt.stem(n,Realen,use_line_collection=True)
    plt.xlabel('n')
    plt.ylabel('Realen del od x[n]')
    plt.show()
    plt.stem(n,Imaginaren,use_line_collection=True)
    plt.xlabel('n')
    plt.ylabel('Imaginaren del od x[n]')
    plt.show()
