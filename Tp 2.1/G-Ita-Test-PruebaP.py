import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot
import numpy as np
import random

parimpar=[]

textoPIm=['PAR','IMPAR']


s1=1234
s2=2934
s0=6153
n=10000
numeros=[]
pn=int(abs(s2-s0))
numeros.insert(0,pn)

def fg(na):
    fnn=int(abs(n-(na*1.99)))
    return fnn

for i in range(1,1000):
    numeros.insert(i,fg(numeros[i-1]))


def prueba_paridad(datos:list):
    par=0
    impar=0
    for i in datos:
        if i % 2 == 0:
            par+=1
        else:
            impar+=1   
    parimpar.insert(0,par)
    parimpar.insert(1,impar)
    print(par)
    print(impar)

def grafT():
    print()



prueba_paridad(numeros)
fig, ax = plt.subplots()
ax.pie(parimpar, labels=textoPIm, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title('Prueba de paridad')
plt.show()


   
