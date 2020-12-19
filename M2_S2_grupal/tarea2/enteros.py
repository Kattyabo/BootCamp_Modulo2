#-*- coding: utf-8 -*-
import random
import numpy as np

caracteres = '0123456789'

# 5)Cree un segundo script enteros.py que contenga una modificación
#del Código Base de tal forma que en lugar de strings, lista contenga
#sólo elementos enteros de largos aleatorios entre 1 y 20 digitos.

lista5 = []
for n in range(0, 10):
    num_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        num_aleatorio += random.choice(caracteres)
    lista5.append(num_aleatorio)
print("\nEsta es la lista 5: \n" + str(lista5))

# 6)Calcule el promedio de los valores numéricos de lista. 
def calcula_largo_promedio(lista5):
    suma_largos = 0
    for elemento in lista5:
        largo = len(elemento)
        suma_largos = suma_largos + largo
    largo_promediol5 = suma_largos/len(lista5)     
    return largo_promediol5

largo_promediol5 = calcula_largo_promedio(lista5)
print("\nLargo promedio de la lista numérica es: " + str(largo_promediol5))

# 7)Actualice lista, restando el promedio a todos los elementos de ésta.

promedio_l5 = calcula_largo_promedio(lista5)
    
lista6 = []    
print("Esta es la listar random - promedio de caracteres:\n")

for n in lista5:
    n = float(n)
    lista5 = lista6
    lista6 = np.array(n)
    lista6 = n - promedio_l5
    print(lista6)
