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
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.savefig('divideAndConquer.png')
