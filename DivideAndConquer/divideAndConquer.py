# A naive recursive Python implementation
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Driver Program to test ht above function
x = []
y = []
z = []    
with open('./values.txt', 'r') as archivo:
    for linea in archivo:
        n, k, t = map(int, linea.strip().split(','))
        z.append(t)
        x.append(n)
        y.append(k)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x, y, z, c='r', marker='o')

# Set labels
ax.set_xlabel('Valor de n')
ax.set_ylabel('Valor de k')
ax.set_zlabel('Tiempo de Ejecución (segundos)')
plt.title('Divide and Conquer - Tiempos de ejecución')
plt.savefig('divideAndConquer.png')
