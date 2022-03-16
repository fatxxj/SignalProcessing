import math

import numpy as np
import matplotlib.pyplot as plt

#TODO: Izrabotil Fat Halimi 2022

t = np.linspace(0,10,1000)
x=[-1,2,-3,0,2,3,-1,5,2,2]
plt.plot(t, np.sin((0.7 *math.pi*t)+0.4))
plt.show()
#Zadaca 1 e objasenta vo Zadaca1-Lab1_195005.py


n=np.asarray(list(range(0,10))) #imame nekoja niza od listi vo opseg 0 do 10
BrPrimeroci=len(n) # zemame dolzina na n ili broj na primeroci
x=np.zeros(BrPrimeroci) # zemame niza od nuli za dadenata dolzina
for i in range (BrPrimeroci): #vrtenje za sekoj od primerocite
    x[i]=np.sin((0.7 *math.pi*BrPrimeroci)+0.4) #za sekoj primerok se izvrsuva funkcijata

plt.stem(0.125*n,x) #povik za generiranje na grafik so stapcinja kade vo sekoja 0.125 ta vrednost ke imame po eden stap
plt.show()#povik za prikaz na generiraniot grafik