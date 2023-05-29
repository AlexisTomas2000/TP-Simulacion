import math
from math import sqrt
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import random
A = 2.6  # Parámetro de forma
K = stats.gamma(A)  # Distribución Gamma con parámetro de forma a
def gammaSR(VA,A):
    TR = 1.0
    for _ in range(VA):
        R = random.random()
        TR *= R
    X = -math.log(TR) / A
    return X
def GammaR(A,K):
    # Variables para el método de rechazo
    c = (1 / (A**A * math.exp(-A)))  # Factor de escala
    M = K.pdf(A) / (c * stats.expon.pdf(A, scale=1))  # Cota superior para el método de rechazo
    x = np.linspace(K.ppf(0.01), K.ppf(0.99), 100)
    fp = K.pdf(x)  # Función de Probabilidad
    aleatorios = []
    i = 0
    while i < 100:
        # Generar un valor aleatorio de la distribución exponencial con parámetro beta=1
        y = random.expovariate(1)
        # Generar un valor aleatorio de una distribución uniforme entre 0 y M
        u = random.uniform(0, M)
        # Calcular el valor propuesto de la distribución gamma
        propuesta = y + A
        # Calcular el factor de aceptación para el método de rechazo
        factor_aceptacion = K.pdf(propuesta) / (c * stats.expon.pdf(y, scale=1))
        # Aceptar o rechazar el valor propuesto
        if u <= factor_aceptacion:
            aleatorios.append(propuesta)
            i += 1   
    return x, fp, aleatorios

def graf(x):
    lis1, lis2, lis3 = GammaR(A,K)
    plt.figure('HisGamma')
    plt.hist(lis3,density=True,bins=50,alpha=0.7,edgecolor='black')
    plt.title('Histograma Distribución Gamma con rechazo')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    
    plt.figure('GrafGamma')
    plt.plot(lis1, lis2)
    plt.title('Distribución Gamma')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    lis4=[gammaSR(100,A) for i in range(100)]
    plt.figure('HisGammaSR')
    plt.hist(lis4,density=True,bins=50,alpha=0.7,edgecolor='black')
    plt.title('Histograma Distribución Gamma sin Rechazo')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
x = np.arange(0, 100, 1)
graf(x)
plt.show()