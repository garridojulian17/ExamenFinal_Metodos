# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
print(x)
impares=[]
imprimir=[]
for i in range(len(x)):
    if(x[i]%2!=0):
        impares.append(x[i])
        if(impares[i]<800):
            imprimir.append(impares[i])
            i=i+1
            print(imprimir)
        
        


