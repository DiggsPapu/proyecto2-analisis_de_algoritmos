# A naive recursive Python implementation
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def binomialCoeff(n, k):

	if k > n:
		return 0
	if k == 0 or k == n:
		return 1

	# Recursive Call
	return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)


# Driver Program to test ht above function
x = []
y = []
z = []    
with open('../pares.txt', 'r') as archivo:
    print("entro")
    for linea in archivo:

        print(linea)
        n, k = map(int, linea.strip().split(','))
        
        init_t = time.time()
        binomialCoe = binomialCoeff(n, k)
        init_t = time.time() - init_t
        z.append(init_t)
        x.append(n)
        y.append(k)
        print("El valor de C[" + str(n) + "][" + str(k) + "] es " + str(binomialCoe))
        print("Tiempo de ejecución: ",  init_t, " segundos")
# for n in range(1,50):
#     for k in range(0, n):
#         x.append(n)
#         y.append(k)
#         init_t = time.time()
#         binomialCoeff(n, k)
#         init_t = time.time() - init_t
#         z.append(init_t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x, y, z, c='r', marker='o')

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show plot
# plt.show()
# n = 30
# for k in range(1,n-1):
#     x.append(k)
#     init_t = time.time()
#     binomialCoeff(n, k)
#     init_t = time.time() - init_t
#     y.append(init_t)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(x, y, c='r', marker='o')
# # Set labels
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# plt.show()
plt.savefig('python1.png')
# print ("Value of C(%d,%d) is (%d)" % (n, k,binomialCoeff(n, k)))

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)
