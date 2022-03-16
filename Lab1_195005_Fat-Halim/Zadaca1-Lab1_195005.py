import math

import numpy as np
import matplotlib.pyplot as plt

#TODO: Izrabotil Fat Halimi 2022


t = np.linspace(0,10,1000) #opseg od 0 do 10 kako prv i vtor argument i tret argument se tockite koi ke se upotrebuvaat za grafikot.

plt.plot(t, np.sin((0.7 *math.pi*t)+0.4))
# prv argument t pretstavuva objekt od opsegot i tockite.
# vtor arugment od biblotekata np povikuva sinus funkcija i vo zagradite e formulata dadena na vezbite,(0.7 *math.pi*t) e staveno vo zagrada od pricina sto sin funkcijata prima 2 argumenti pa soodvetno (0.7 *math.pi*t) e prv argument i 0,4 e vtor.
plt.show() #povik za da se generira grafikot.

