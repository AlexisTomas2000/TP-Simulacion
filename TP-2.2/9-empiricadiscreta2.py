import random
import numpy as np
import matplotlib.pyplot as plt

def empirica_discreta(values, probabilities, n):
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    random_values = []
    
    for _ in range(n):
        random_value = random.random()
        
        for i, cumulative_prob in enumerate(cumulative_probabilities):
            if random_value < cumulative_prob:
                random_values.append(values[i])
                break
    
    return random_values
def empirica_discretaCR(values, probabilities, n):
    random_values = []
    max_probability = max(probabilities)

    while len(random_values) < n:
        random_index = random.randint(0, len(values) - 1)
        random_probability = random.uniform(0, max_probability)

        if random_probability <= probabilities[random_index]:
            random_values.append(values[random_index])

    return random_values


# Ejemplo de uso
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
probabilities = [0.1, 0.3, 0.05, 0.05, 0.2, 0.03, 0.07, 0.08, 0.02]
num_values = 1000

random_numbers = empirica_discreta(values, probabilities, num_values)
print(random_numbers)
random_numbersCR=empirica_discretaCR(values, probabilities, num_values)
print(random_numbersCR)
plt.figure('HistogramaSR')
plt.hist(random_numbers, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Distribución Empirica Discreta')
plt.figure('HistogramaCR')
plt.hist(random_numbersCR, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Distribución Empirica Discreta con Rechazo')
plt.show()