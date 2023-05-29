import math
import random
from matplotlib import pyplot as plt
from scipy.stats import poisson
import numpy as np
p=3
def poissn(p):
    x = 0
    L = math.exp(-p)
    tr = 1.0
    while True:
        tr *= random.random()
        if tr <= L:
            return x
        else:
            x += 1

def poissnR():
    numeros = []
    l = 3  # lambda
    for i in range(1000):
        u = random.random()
        x = 0
        P = F = math.exp(-l)
        while u >= F:
            P = (l / (x + 1)) * P
            F = F + P
            x = x + 1
        numeros.append(x)
    return numeros

# Generar las muestras
NcrP = poissnR()
NsrP = [poissn(3) for i in range(1000)]

# Calcular las frecuencias observadas y esperadas
Fre_obs, _ = np.histogram(NsrP, bins=range(max(NsrP)+2))
Fre_esp = [poisson.pmf(x, 3) * 1000 for x in range(len(Fre_obs))]

# Calcular el estadístico chi-cuadrado
chi_cuad = sum((Fre_obs - Fre_esp) ** 2 / Fre_esp)

# Calcular los grados de libertad
gl = len(Fre_obs) - 1

# Calcular el valor crítico de chi-cuadrado
valorCritico = poisson.ppf(0.95, gl)

# Imprimir resultados
print("Estadístico Chi-cuadrado:", chi_cuad)
print("Valor crítico:", valorCritico)

# Comparar el estadístico chi-cuadrado con el valor crítico
if chi_cuad > valorCritico:
    print("Se rechaza la hipótesis nula. Las muestras no siguen una distribución de Poisson.")
else:
    print("No se puede rechazar la hipótesis nula. Las muestras siguen una distribución de Poisson.")


# Mostrar los histogramas
plt.figure('HistogramasinR')
plt.hist(NsrP)
plt.grid(True)
plt.figure('HistogramaconR')
plt.hist(NcrP)
plt.grid(True)
plt.figure('GrafPoisson')
x = np.arange(0, 21)
probabilidades = poisson.pmf(x, p)
plt.plot(x, probabilidades)
plt.title('Distribución de Poisson')
plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()
plt.show()