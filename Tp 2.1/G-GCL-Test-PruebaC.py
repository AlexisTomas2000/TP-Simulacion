import numpy as np
from scipy.stats import chi2
import math


a=25214903917
c=11
m=2**48
xo=2025
aleatorios=[]
aleatorios.insert(0,xo)

def gcl(a,c,m,xo):
    nro=(a*xo +c) % m
    return nro

for i in range(1,1000):
    aux = gcl(a,c,m,aleatorios[i-1])
    y=len(str(aux))
    aleatorios.insert(i,int(str(aux)[y-4:y]))
print(aleatorios)


def count_runs(numeros):
    runs = 1
    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i-1]:
            if i == len(numeros) - 1:
                runs += 1
            elif numeros[i+1] < numeros[i]:
                runs += 1
        elif numeros[i] < numeros[i-1]:
            if i == len(numeros) - 1:
                runs += 1
            elif numeros[i+1] > numeros[i]:
                runs += 1
    return runs

def media(numeros):
    N = len(numeros)
    media = ((2*N)-1)/3
    return media

def desvio(numeros):
    N = len(numeros)
    desvio = ((16*N)-29)/90
    return desvio

def pruebacolas(media, desvio, runs):
    z = ((runs - media)/(math.sqrt(desvio)))
    return z

#Ejecucion

runs = count_runs(aleatorios)
print(runs)
valor_media = media(aleatorios)
print(valor_media)
valor_desvio = desvio(aleatorios)
print(valor_desvio)
z = pruebacolas(valor_media, valor_desvio, runs)
print(z)


