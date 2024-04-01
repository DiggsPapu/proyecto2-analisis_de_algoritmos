import time
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os

print("Directorio actual:", os.getcwd())

tiempos_ejecucion = []
valores_n = []
valores_k = []

def binomialCoeffUtil(n, k, dp):
    if dp[n][k] != -1:
        return dp[n][k]

    if k == 0:
        dp[n][k] = 1
        return dp[n][k]

    if k == n:
        dp[n][k] = 1
        return dp[n][k]

    dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
                binomialCoeffUtil(n - 1, k, dp))

    return dp[n][k]

def binomialCoeff(n, k):
    n = int(n)
    k = int(k)
    dp = [[-1 for y in range(k + 1)] for x in range(n + 1)]

    startTime = time.time()
    binomialCoefficient = binomialCoeffUtil(n, k, dp)
    endTime = time.time()
    totalExcTime = endTime - startTime

    valores_n.append(n)
    valores_k.append(k)
    tiempos_ejecucion.append(totalExcTime)

    return binomialCoefficient, totalExcTime

with open('pares.txt', 'r') as archivo:
    print("entro")
    for linea in archivo:
        print(linea)
        n, k = map(int, linea.strip().split(','))

        binomialCoe, ExcTime = binomialCoeff(n, k)

        print("El valor de C[" + str(n) + "][" + str(k) + "] es " + str(binomialCoe))
        print("Tiempo de ejecución: ", ExcTime, " segundos")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar en 3D
ax.scatter(valores_n, valores_k, tiempos_ejecucion, c='r', marker='o')

ax.set_xlabel('Valor de n')
ax.set_ylabel('Valor de k')
ax.set_zlabel('Tiempo de Ejecución (segundos)')

plt.title('Tiempo de Ejecución del Programa')

plt.show()
