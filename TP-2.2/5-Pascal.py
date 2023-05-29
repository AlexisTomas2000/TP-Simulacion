import random
import math
import matplotlib.pyplot as plt
import numpy as np
def pascal(K, Q):
    TR = 1.0
    QR = math.log(Q)
    for I in range(1, K + 1):
        R = random.random()
        TR = TR * R
    NX = math.log(TR) / QR
    X = NX
    return X

def pascalR(K, Q):#MetodoRechazo
    while True:
        # Generar un valor de la distribución exponencial negativa
        Y = -math.log(random.random()) / Q

        # Generar un número de éxitos según la distribución geométrica
        X = 0
        U = random.random()
        while U >= math.exp(-K * Q):
            U *= random.random()
            X += 1

        # Si el número de éxitos es igual a K, aceptar el valor generado
        if X == K:
            return Y

# Definir los parámetros de la distribución Pascal
K = 5  # Número de éxitos requeridos
Q = 0.1  # Probabilidad de éxito en cada ensayo

# Generar valores de la distribución Pascal utilizando el método de rechazo
num_valores = 1000  # Número de valores a generar
valores_pascal = [pascalR(K, Q) for _ in range(num_valores)]
valores_pascal2 = [pascal(K, Q) for _ in range(num_valores)]
plt.figure('SinMetodoRec')
plt.hist(valores_pascal2,density=True,bins=50,alpha=0.7,edgecolor='black')
plt.title('Histograma de la distribución Pascal sin rechazo')
plt.grid()
plt.ylabel('Frecuencia')
plt.xlabel('Valores')
plt.figure('ConMetodoRec')
plt.hist(valores_pascal,density=True,bins=50,alpha=0.7,edgecolor='black')
plt.title('Histograma de la distribución Pascal con rechazo')
plt.grid()
plt.ylabel('Frecuencia')
plt.xlabel('Valores')
plt.figure('GrafPAs')
# Valores x: número de ensayos hasta el k-ésimo éxito
x = np.arange(0, 101)  # Rango de valores para graficar

# Probabilidades correspondientes a cada valor x
probabilities = np.array([Q ** K * (1 - Q) ** (n - K) for n in x])

# Graficar la distribución de Pascal
plt.plot(x, probabilities, color='r')

# Configurar etiquetas y título del gráfico
plt.xlabel('Número de ensayos')
plt.ylabel('Probabilidad')
plt.title('Distribución de Pascal')
plt.show()



