#-*- coding: utf-8 -*-
import random
caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz­_'


# 1)El usuario indica 'random', crea largo 'random' para el string
largo_listas = 5
lista = []
for n in range(0, 100):
    string_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)
print("\n" + str(lista))


# 3)Función promedio de lista de caracteres
def calcula_largo_promedio(lista):
    suma_largos = 0
    for elemento in lista:
        largo = len(elemento)
        suma_largos = suma_largos + largo
    largo_promedio = suma_largos/len(lista)     
    return largo_promedio

largo_promedio = calcula_largo_promedio(lista)
print("\nLargo promedio de la lista es: " + str(largo_promedio))


# 2)Lista que entrega random caracteres, pero con 
#el mismo n° de caracteres que lista anterior.
lista2 = []
for n in range(0, largo_listas):
    string_aleatorio = ''
    largo = len(lista[n])
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista2.append(string_aleatorio)
print("\n" + str(lista2) + "\n")


#Creación de nueva lista con n° caracteres por string iguales
truncar_a_entero = int(largo_promedio)


# 4)Lista que entrega random caracteres, pero con 
#el mismo n° de caracteres del n° de enteros promedio anterior.
lista3 = []
for n in range(0, largo_listas):
    string_aleatorio = ''
    largo = truncar_a_entero
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista3.append(string_aleatorio)
print("\n" + str(lista3) + "\n")