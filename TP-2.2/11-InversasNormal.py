import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv
from scipy import stats

def t_inversa_normal(n):
    u = np.random.uniform(0, 1, n)  # Genera n números aleatorios uniformes
    x = np.sqrt(2) * erfinv(2 * u - 1)  # Aplica la transformación inversa
    return x

# Genera 10,000 muestras utilizando la transformada inversa
samples = t_inversa_normal(1000)
print(samples)

def TestKolmogorovSmirnov(vn, EX, STDX):
    ks_statistic, p_value = stats.kstest(vn, 'norm', args=(EX, STDX))
    alpha = 0.05
    if p_value < alpha:
        print('La muestra no sigue una distribución normal')
    else:
        print('La muestra sigue una distribución normal')

    print('KS Statistic:', ks_statistic)
    print('P-value:', p_value)

# Visualización del histograma
plt.hist(samples, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Distribución Normal')
plt.show()
TestKolmogorovSmirnov(samples,10,1)
