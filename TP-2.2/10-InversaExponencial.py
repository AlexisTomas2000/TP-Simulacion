import numpy as np
import matplotlib.pyplot as plt

def t_inversa_exp(lam, n):
    u = np.random.uniform(0, 1, n)  # Genera n números aleatorios uniformes
    x = -np.log(1 - u) / lam  # Aplica la transformada inversa
    return x

# Parámetro de tasa lambda
lam = 0.5

# Genera 10,000 muestras utilizando la transformada inversa
samples = t_inversa_exp(lam, 10000)

# Visualización del histograma
plt.hist(samples, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Distribución Exponencial')
plt.show()