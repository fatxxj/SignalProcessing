import math

import numpy as np
import matplotlib.pyplot as plt

#TODO: Izrabotil Fat Halimi 2022


t = np.linspace(0,10,1000)
x=[-1,2,-3,0,2,3,-1,5,2,2]
plt.plot(t, np.sin((0.7 *math.pi*t)+0.4))
plt.show()

#Zadaca 1 e objasenta vo Zadaca1-Lab1_195005.py

n=list(range(0,10)) #generirame lista od opsegot od 0 do 10
BrPrimeroci=len(n) # zemame dolzina na soodvetnata  lista (kolku promenlivi imame) koja ja imame vo promenlivata n
x=np.zeros(BrPrimeroci)  #zemame niza od nuli so dadenata dolzina
for i in range (BrPrimeroci): #ciklus za da se vrti niz site promenlivi
    x[i]=np.sin((0.7 *math.pi*BrPrimeroci)+0.4) #za sekoja od promenlivite se presmetuva funkcijata

plt.stem(n,x) # povik za generiranje na grafik so stapcinja
plt.show() # povik za prikaz na grafikot vo ekran