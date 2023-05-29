import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot
import numpy as np
import random


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


def prueba_corridas_medias(datos):
    nrosmasmedia = 0
    numerosmenosmedia = 0
    media1 = np.mean(datos)
    for i in datos:
        if i > media1:
            nrosmasmedia +=1
        else:
            numerosmenosmedia+=1
    print("cambio")
    print(nrosmasmedia)
    print(numerosmenosmedia) 
    n = len(datos)
    media = (((2 * nrosmasmedia * numerosmenosmedia)) / (numerosmenosmedia + nrosmasmedia)) + 1  # Cálculo de la media
    s = ((2 * nrosmasmedia * numerosmenosmedia)*((2 * nrosmasmedia * numerosmenosmedia)- n)) / ((n**2)*(n-1)) # Cálculo de la desviación estándar
    print('Media:'+ str(media))
    print('Desviación estándar:'+ str(s))

    # Contar el número de corridas
    bits = []
    n = len(datos)
    for i in range(1, n):
        if numeros[i] > numeros[i-1]:
            bits.append(1)
        else:
            bits.append(0)
    
    print(bits)
    n= len(bits)
    corridas = 1
    for i in range(1, n):
        if bits[i] != bits[i-1]:
            corridas += 1

    print(corridas)
    print(media)
    print(s)
    # Calcular el valor z
    z = (corridas - media) / (s)
    print('Z:')
    print(z)
    # Imprimir resultados
    if z <= 1.9599:
        print("Los datos son aleatorios.")
    else:
        print("Los datos no son aleatorios.")
        

prueba_corridas_medias(numeros)



