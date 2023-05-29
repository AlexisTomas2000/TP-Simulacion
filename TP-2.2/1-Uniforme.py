from matplotlib import pyplot as plt
import random
import numpy as np
from scipy.stats import kstest

b = 5
a = 2
size = 10000

def Uniforme(size):  # Dist. Uniforme
    ListUni = []
    for i in range(size):
        nr = random.random()
        vu = round(a + nr * (b - a), 4)
        ListUni.append(vu)
    return ListUni
def runiforme(size, a, b):
    ListUni = []
    while len(ListUni) < size:
        u = random.random()
        x = a + u * (b - a)
        y = random.random()
        if y <= 1 / (b - a):
            ListUni.append(x)
    return ListUni


def DUni(x):
    return 1/3  # (a+b)/2


def TestKolmogorovSmirnov(muestra):
    ks_statistic, p_value = kstest(muestra, 'uniform', args=(0, 100))
    alpha = 0.05
    if p_value < alpha:
        print('La muestra no sigue una distribución uniforme')
    else:
        print('La muestra sigue una distribución uniforme')

    print('KS Statistic:', ks_statistic)
    print('P-value:', p_value)


def fun(x):
    if x <= a:
        return 0
    elif a < x < b:
        p = (x - a) / (b - a)
        return p
    else:
        return 1


def gra(x,a):
    if a==1:
        return 1 / 3
    else:
        return 1/3


def graf(x, p):
    if p == 1:
        nor = Uniforme(size)
        plt.figure('histo')
        plt.hist(nor, label='Muestras generadas',density=True,bins=50,alpha=0.7,edgecolor='black')
        plt.ylabel('Frecuencia')
        plt.xlabel('Valores')
        plt.axhline(y=gra(1,1), color='r')
        plt.plot(x,[gra(i,2) for i in x])
        plt.grid(True)
        plt.figure('Grafica de la distribucion')
        plt.axhline(y=gra(1,1), color='r')
        plt.ylabel('Valor esperado')
        plt.xlabel('Valores')
        plt.grid(True)
        nor2=runiforme(size,a,b)
        plt.figure('Histograma Distribución Uniforme con rechazo')
        plt.hist(nor2, label='Muestras generadas',density=True,bins=50,alpha=0.7,edgecolor='black')
        plt.ylabel('Frecuencia')
        plt.xlabel('Valores')
        plt.title('Histograma Distribución Uniforme con rechazo')
        plt.axhline(y=gra(1,1), color='r')
        plt.grid(True)
        TestKolmogorovSmirnov(nor)
        print('Re')
        TestKolmogorovSmirnov(nor2)
       

x = np.arange(2, 5, 0.5)
graf(x, 1)
plt.show()