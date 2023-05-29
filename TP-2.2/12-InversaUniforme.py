import numpy as np
import matplotlib.pyplot as plt

def inverse_transform_sampling(a, b, n):
    u = np.random.uniform(0, 1, n)  # Genera n números aleatorios uniformes
    x = a + (b - a) * u  # Aplica la transformada inversa
    return x

# Parámetros del intervalo [a, b]
a = 2
b = 5

# Genera 10,000 muestras utilizando la transformada inversa
samples = inverse_transform_sampling(a, b, 10000)

# Visualización del histograma
plt.hist(samples, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Distribución Uniforme')
plt.show()