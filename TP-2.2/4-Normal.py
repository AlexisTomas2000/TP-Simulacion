import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
EX=10
STDX=1
def normal(EX, STDX):
    SUM = 0.0
    for _ in range(12):
        R = random.random()
        SUM += R

    X = EX + STDX * (SUM - 6.0)
    return X

def normalR(EX, STDX):
    while True:
        SUM = 0.0
        for _ in range(12):
            R = random.random()
            SUM += R

        X = EX + STDX * (SUM - 6.0)

        # Generar un valor aleatorio U entre 0 y 1
        U = random.random()

        # Calcular la función de densidad de probabilidad (PDF) de una distribución normal estándar en X
        PDF_X = (1 / (math.sqrt(2 * math.pi) * STDX)) * math.exp(-(X - EX)**2 / (2 * STDX**2))

        # Comprobar si U está por debajo de la PDF_X
        if U <= PDF_X:
            return X

def TestKolmogorovSmirnov(vn, EX, STDX):
    ks_statistic, p_value = stats.kstest(vn, 'norm', args=(EX, STDX))
    alpha = 0.05
    if p_value < alpha:
        print('La muestra no sigue una distribución normal')
    else:
        print('La muestra sigue una distribución normal')

    print('KS Statistic:', ks_statistic)
    print('P-value:', p_value)

def Graf():
    NsR=[normal(EX,STDX) for i in range(1000)]
    NcR=[normalR(EX,STDX) for i in range(1000)]
    plt.figure('Normal sin rechazo')
    plt.hist(NsR,20)
    plt.grid(True)
    plt.figure('Normal con rechazo')
    plt.hist(NcR,20)
    plt.grid(True)
    plt.figure('Grafica distribucion normal')
    x = np.linspace(EX - 3 * STDX, EX + 3 * STDX, 100)
    # Calcular la función de densidad de probabilidad (PDF) de la distribución normal
    pdf = (1 / (STDX * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - EX) / STDX)**2)
    # Graficar la distribución normal
    plt.plot(x, pdf)
    plt.xlabel('Valores')
    plt.ylabel('Densidad de Probabilidad')
    plt.title('Distribución Normal')
    print('Sin rechazo')
    TestKolmogorovSmirnov(NsR,EX,STDX)
    print('Con rechazo')
    TestKolmogorovSmirnov(NcR,EX,STDX)
    plt.show()
Graf()