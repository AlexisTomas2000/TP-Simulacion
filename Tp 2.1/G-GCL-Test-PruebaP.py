import matplotlib.pyplot as plt
import numpy as np

a=25214903917
c=11
m=2**48
xo=2025
numeros=[]
numeros.insert(0,xo)
parimpar=[]

textoPIm=['PAR','IMPAR']

def gcl(a,c,m,xo):
    nro=(a*xo +c) % m
    return nro

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

def grafT():
    print()


for i in range(1,1000):
    aux = gcl(a,c,m,numeros[i-1])
    y=len(str(aux))
    numeros.insert(i,int(str(aux)[y-4:y]))


prueba_paridad(numeros)
fig, ax = plt.subplots()
ax.pie(parimpar, labels=textoPIm, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title('Prueba de paridad')
plt.show()


