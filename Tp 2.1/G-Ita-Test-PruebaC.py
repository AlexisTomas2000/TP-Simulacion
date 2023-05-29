import numpy as np
from scipy.stats import chi2
import math


s1=1234
s2=2934
s0=6153
n=10000
aleatorios=[]
pn=int(abs(s2-s0))
aleatorios.insert(0,pn)

def fg(na):
    fnn=int(abs(n-(na*1.99)))
    return fnn
for i in range(1,1000):
    aleatorios.insert(i,fg(aleatorios[i-1]))


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
    z = (runs - media)/(desvio ** 0.5)
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
