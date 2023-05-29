import math
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import random

size = 1000  # Tamaño de la muestra
media = 1.0 
def Exponencial(media):
    R = random.random()
    X = -media * math.log(R)
    return X
def RExponencial(media, size): # Método de rechazo para distribución exponencial
    ListExp = []
    while len(ListExp) < size:
        u = random.random()
        v = -media * math.log(u)
        if u <= math.exp(-v / media):
            ListExp.append(v)
    return ListExp

def t_inversa_exp(lam, n):
    u = np.random.uniform(0, 1, n)  # Genera n números aleatorios uniformes
    x = -np.log(1 - u) / lam  # Aplica la transformada inversa
    return x

def TestKolmogorovSmirnov(ve, media):
    ks_statistic, p_value = stats.kstest(ve, 'expon', args=(0, media))
    alpha = 0.05
    if p_value < alpha:
        print('La muestra no sigue una distribución exponencial')
    else:
        print('La muestra sigue una distribución exponencial')

    print('KS Statistic:', ks_statistic)
    print('P-value:', p_value)

def graf():
    ve = [Exponencial(media) for i in range(1000)]
    plt.figure('DisExpcR')
    plt.hist(ve, bins='auto', density=True)

    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma Distribución Exponencial sin rachazo')
    plt.grid(True)

    exponencial = stats.expon(scale=1/media)
    q = np.linspace(exponencial.ppf(0.01), exponencial.ppf(0.99), 100)
    fp = exponencial.pdf(q)
    plt.figure('Grafica')
    plt.plot(q, fp)
    plt.title('Distribución Exponencial')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    ve2 = RExponencial(media, size)
    plt.figure('DisExpsR')
    plt.hist(ve2, bins=50, density=True, alpha=0.7, edgecolor='black')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma Distribución Exponencial con rachazo')
    plt.grid(True)
    ve3 = t_inversa_exp(media, size) 
    TestKolmogorovSmirnov(ve, media)
    TestKolmogorovSmirnov(ve2, media)
    TestKolmogorovSmirnov(ve3, media)
    plt.show()

graf()