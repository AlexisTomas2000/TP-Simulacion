import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def binom(N, P):
    X = 0.0
    for I in range(1, N+1):
        R = random.random()
        if R - P < 0:
            X = X + 10
    return X
def binomR(N, P):
    X = 0
    for _ in range(N):
        R = random.random()
        if R < P:
            X += 1
    return X
def Chicuadrado(frec_obs,frec_esp):
    # Realizar el test de chi-cuadrado
    statistic,p_valor=stats.chisquare(frec_obs,f_exp=frec_esp)
    print("Resultado del test de chi-cuadrado:")
    print("Estadístico de chi-cuadrado:", statistic)
    print("Valor p:", p_valor)
    if p_valor > 0.05:
        print("No se rechaza la hipótesis nula: los valores siguen una distribución binomial.")
    else:
        print("Se rechaza la hipótesis nula: los valores no siguen una distribución binomial.")
# Definir los parámetros de la distribución binomial
N = 100  # Número de ensayos
P = 0.10  # Probabilidad de éxito en cada ensayo
num_valores = 1000  # Número de valores a generar

# Generar los valores binomiales
lvb = [binom(N, P) for _ in range(num_valores)]
lvb1=[binomR(N, P) for _ in range(num_valores)]
# Definir los intervalos
intervalos = range(0, 251, 10)

# Calcular las frecuencias observadas
frecuencias_obs, _ = np.histogram(lvb, bins=intervalos, density=True)
frecuencias_obs2, _ = np.histogram(lvb1, bins=intervalos, density=True)
# Calcular las frecuencias esperadas
frecuencias_esp = [num_valores * P] * len(intervalos[:-1])

# Graficar las frecuencias observadas
plt.figure('Histograma sin rechazo')
plt.hist(lvb,density=True,bins=50,alpha=0.7,edgecolor='black')
plt.xlabel('Intervalos')
plt.ylabel('Frecuencias')
plt.title('Histograma distribucion binomial sin rechazo')

plt.figure('Histograma con rechazo')
plt.hist(lvb1,density=True,bins=50,alpha=0.7,edgecolor='black')
plt.xlabel('Intervalos')
plt.ylabel('Frecuencias')
plt.title('Histograma distribucion binomial con rechazo')

# Crear un arreglo de valores posibles para X (número de éxitos)
plt.figure('Grafica')
x = np.arange(50,151,1)

# Calcular la probabilidad de cada valor de X en la distribución binomial
probabilidades = [stats.binom.pmf(i, N*10, P) for i in x]

# Graficar la distribución binomial
plt.plot(x, probabilidades, color='b')
plt.xlabel('Número de Éxitos')
plt.ylabel('Probabilidad')
plt.title('Distribución Binomial')
#Prueba rechazo chi2
frecuencia= {}
for fre in set(lvb):
    frecuencia[fre]=lvb.count(fre)
frecuencia1= {}
for fre in set(lvb1):
    frecuencia1[fre]=lvb1.count(fre)
# Obtener la lista de frecuencias observadas
frec_obs = list(frecuencia.values())
frec_obs1 = list(frecuencia1.values())
# Definir las frecuencias esperadas (por ejemplo, una distribución uniforme)
nv = len(lvb)
nv1=len(lvb1)
frec_esp = [nv / len(set(lvb))] * len(set(lvb))
frec_esp1 = [nv1 / len(set(lvb1))] * len(set(lvb1))
Chicuadrado(frec_obs,frec_esp)
Chicuadrado(frec_obs1,frec_esp1)
plt.show()