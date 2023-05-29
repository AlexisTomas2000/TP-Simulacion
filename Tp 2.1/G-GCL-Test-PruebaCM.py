import matplotlib.pyplot as plt
import numpy as np

a=25214903917
c=11
m=2**48
xo=2025
numeros=[]
numeros.insert(0,xo)


def gcl(a,c,m,xo):
    nro=(a*xo +c) % m
    return nro

def prueba_corridas_medias(datos):
    nrosmasmedia = 0
    numerosmenosmedia = 0
    media1 = np.mean(datos)
    for i in datos:
        if i > media1:
            nrosmasmedia +=1
        else:
            numerosmenosmedia+=1
    print(nrosmasmedia)
    print(numerosmenosmedia) 
    n = len(datos)
    media = (((2 * nrosmasmedia * numerosmenosmedia)) / (numerosmenosmedia + nrosmasmedia)) + 1  # Cálculo de la media
    s = ((2 * nrosmasmedia * numerosmenosmedia)*((2 * nrosmasmedia * numerosmenosmedia)- n)) / ((n**2)*(n-1)) # Cálculo de la desviación estándar
    print('Media:'+ str(media))
    print('Desviación estándar:'+ str(s))

    # Contar el número de corridas
    bits = []
    n = len(datos)
    for i in range(1, n):
        if numeros[i] > numeros[i-1]:
            bits.append(1)
        else:
            bits.append(0)
    
    print(bits)
    n= len(bits)
    corridas = 1
    for i in range(1, n):
        if bits[i] != bits[i-1]:
            corridas += 1

    print(corridas)
    print(media)
    print(s)
    # Calcular el valor z
    z = (corridas - media) / (s)
    print('Z:')
    print(z)
    # Imprimir resultados
    if z <= 1.9599:
        print("Los datos son aleatorios.")
    else:
        print("Los datos no son aleatorios.")


for i in range(1,1000):
    aux = gcl(a,c,m,numeros[i-1])
    y=len(str(aux))
    numeros.insert(i,int(str(aux)[y-4:y]))
        

prueba_corridas_medias(numeros)



