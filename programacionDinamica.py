import time
import matplotlib.pyplot as plt
import os

print("Directorio actual:", os.getcwd())

tiempos_ejecucion=[]

def binomialCoeffUtil(n, k, dp):
     
    # If value in lookup table then return 
    if dp[n][k] != -1: 
        return dp[n][k] 
 
    # Store value in a table before return 
    if k == 0:
        dp[n][k] = 1
        return dp[n][k] 
     
    # Store value in table before return 
    if k == n: 
        dp[n][k] = 1
        return dp[n][k] 
     
    # Save value in lookup table before return 
    dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
                binomialCoeffUtil(n - 1, k, dp))
                 
    return dp[n][k] 
 
def binomialCoeff(n, k):
    n= int(n)
    k= int(k)
     
    # Make a temporary lookup table 
    dp = [ [ -1 for y in range(k + 1) ] 
                for x in range(n + 1) ] 
    
    startTime= time.time()

    binomialCoefficient= binomialCoeffUtil(n,k,dp)

    endTime= time.time()
    totalExcTime= endTime - startTime

    return binomialCoefficient, totalExcTime


with open('pares.txt', 'r') as archivo:
    print("entro")
    for linea in archivo:

        print(linea)
        n, k = map(int, linea.strip().split(','))
        
        binomialCoe, ExcTime= binomialCoeff(n, k)

        tiempos_ejecucion.append(ExcTime)

        print("El valor de C[" + str(n) + "][" + str(k) + "] es " + str(binomialCoe))
        print("Tiempo de ejecución: ",  ExcTime, " segundos")

# Graficar los tiempos de ejecución
plt.plot(tiempos_ejecucion, marker='o')
plt.xlabel('Iteración')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempo de Ejecución del Programa')
plt.grid(True)
plt.show()