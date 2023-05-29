import random
from matplotlib import pyplot as plt
from scipy.stats import hypergeom
import numpy as np
# Parámetros de la distribución hipergeométrica
TN = 1000  # Tamaño de la población
NS = 100   # Tamaño de la muestra
P = 0.1    # Probabilidad de éxito en la población
def hipergeometrica(TN, NS, P):
    while True:
        X = 0
        for _ in range(NS):
            R = random.random()
            if R < P:
                X += 1
        if X <= TN:
            return X

def rechazo_hipergeometrica(TN, NS, P, n):
    resultados = []
    while len(resultados) < n:
        Y = hipergeometrica(TN, NS, P)
        U = random.random()
        if U < Y / NS:
            resultados.append(Y)
    return resultados
def grafica_distribucion_hipergeometrica(TN, NS, P):
# Parámetros de la distribución hipergeométrica
    N = TN  # Tamaño de la población
    n = int(P * N)  # Número de elementos en la población con la propiedad
    m = NS  # Tamaño de la muestra
    x = np.arange(max(0, m - (N - n)), 21,1)  # Valores posibles de la variable aleatoria

    # Calcular la probabilidad de cada valor en x
    pmf = hypergeom.pmf(x, N, n, m)

    # Graficar la distribución hipergeométrica
    plt.figure('Grafico de barras')
    plt.bar(x,pmf)
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.title('Distribución Hipergeométrica (Histograma)')
    plt.grid(True)
    plt.plot(x, pmf, 'bo-', ms=8, label='PMF')  
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.title('Distribución Hipergeométrica (Gráfica)')
    plt.legend()
    # Generar 1000 valores utilizando el método de rechazo para la distribución hipergeométrica
    resultadosR = rechazo_hipergeometrica(TN, NS, P, 1000)
    resultadosSR=[hipergeometrica(TN,NS,P) for i in range(1000)]

    # Graficar
    plt.figure('HiperConRechazo')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma Distribución Hipergeometrica con Rechazo')
    plt.hist(resultadosR, bins=50, density=True, alpha=0.7, edgecolor='black')
    plt.grid(True)
    plt.figure('HiperSinRechazo')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma Distribución Hipergeometrica')
    plt.hist(resultadosSR, bins=50, density=True, alpha=0.7, edgecolor='black')
    plt.grid(True)
    plt.show()

grafica_distribucion_hipergeometrica(TN,NS,P)