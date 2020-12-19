#-*- coding: utf-8 -*-
import random
import numpy as np

# 8)Cree un tercer script floats.py que contenga una modificación del
# Código Base de tal forma que en lugar de strings, lista contenga sólo
# números flotantes aleatorios entre 10 y 50 con 3 decimales.

lista7 = []
print("\nEsta es la lista 7 de float 3 decimales:")

for i in range(0, 10):
    x = round(random.uniform(10.10, 50.50), 3)
    lista7.append(x)

print(lista7)
print("\n")

# 9)Actualice lista, normalizando sus elementos restándole el promedio
# y dividiéndolos por el valor máximo. Obtenga la suma de todos los
# elementos de lista.

lista8 = []
print("\nEsta es la lista 8:")

for i in range(0, 10):
    x = round(random.uniform(10.10, 50.50), 3)
    lista8.append(x)
print(lista8)

lista8a = []
for elemento in lista8:
    sum(lista8)
    promedio_l8 = sum(lista8)/10    
print("\nPromedio de la lista float es: " + str(promedio_l8))

max_l8 = max(lista8)
print("\nMáximo de la lista float es: " + str(max(lista8)) +"\n")

print("\nEsta es la lista 8 de float menos el promedio y dividiendo el valor máximo:")

lista8a = []
for n in lista8:
    n = float(n)
    lista8 = lista8a
    lista8a = np.array(n)
    lista8a = (n - promedio_l8) / max_l8
    print(lista8a)

print("\nEsta es la lista 8 de float menos el promedio, dividiendo el valor máximo y suma los valores:")

print(round(lista8a, 2))
print('\n')
