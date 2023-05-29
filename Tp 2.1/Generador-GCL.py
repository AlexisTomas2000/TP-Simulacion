
a = 25214903917
c = 11
m = 2**48
xo = 2025
numeros = []
numeros.insert(0, xo)


def gcl(a, c, m, xo):
    nro = (a*xo + c) % m
    return nro


for i in range(1, 1000):
    aux = gcl(a, c, m, numeros[i-1])
    y = len(str(aux))
    numeros.insert(i, int(str(aux)[y-4:y]))