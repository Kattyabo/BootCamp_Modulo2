import time
import os
import sys
# os y sys se importan para funcion clear

#Haga una lista llamada ordenes_de_sandwiches y llénela con 20 líneas
#con nombres de 5 tipos de sandwiches. Luego haga una lista vacía
#llamada sandwiches_terminados. Recorra con un loop la lista
#ordenes_de_sandwiches e imprima un mensaje para cada pedido, como
#“Su sandwich de atún ya está preparado”. A medida que se termina de
#preparar cada sandwich, el programa debe moverlo a la lista
#sandwiches_terminados. Una vez preparados todos los sándwiches,
#imprima un mensaje que enumere cada sandwich que se preparó.

sp = ["1.Italiano", "2.Chacarero", "3.Barros_Luco", "4.Dinámico", "5.Suizo"]
sandwiches_terminados = []
tipo_sandwich = []
contador = 0

print("\n Bienvenidos, favor elija el sandwich de nuestra lista: ")
while len(tipo_sandwich) < 5:
    tipo_sandwich = str(input("\n\t 1 Italiano \n\t 2 Chacarero \n\t 3 Barros_Luco \n\t 4 Dinámico \n\t 5 Suizo \n\t SALIR \n"))
    if tipo_sandwich == "1":
        print("Su sandwich " + str(sp[0]) + " ya esta preparado \n")
    elif tipo_sandwich == "2":
        print("Su sandwich " + str(sp[1]) + " ya esta preparado \n")
    elif tipo_sandwich == "3":
        print("Su sandwich " + str(sp[2]) + " ya esta preparado \n")
    elif tipo_sandwich == "4":
        print("Su sandwich " + str(sp[3]) + " ya esta preparado \n")
    elif tipo_sandwich == "5":
        print("Su sandwich " + str(sp[4]) + " ya esta preparado \n")
    else:  
        tipo_sandwich == "salir"
        sandwich_terminados = len(tipo_sandwich) < 5
        print("¡Gracias por su compra!")
        continue

print(tipo_sandwich)
print(sandwiches_terminados)

# Luego, utilizando la lista ordenes_de_sandwiches, asegúrese de que el
# sandwich 'Barros Luco' aparece en la lista al menos tres veces. Agregar
# código cerca del comienzo de su programa para imprimir un mensaje
# que diga que el local se ha quedado sin “Barros Luco”. Luego use un
# loop while para eliminar todas las apariciones de 'Barros Luco' de
# ordenes_de_sandwiches. Asegúrese de que no terminen los sándwiches
# “Barros Luco” en sandwiches terminados.

sp = ["1.Italiano", "2.Chacarero", "3.Barros_Luco", "4.Dinámico", "5.Suizo"]
sandwiches_terminados = 0
tipo_sandwich = []

print("\n Bienvenidos, favor elija el sandwich de nuestra lista: ")
while len(sandwiches_terminados) < 20:
    tipo_sandwich = str(input("\n\t 1 Italiano \n\t 2 Chacarero \n\t 3 Barros_Luco \n\t 4 Dinámico \n\t 5 Suizo \n\t SALIR \n"))
    if tipo_sandwich == "1":
        print("Su sandwich " + str(sp[0]) + " ya esta preparado \n")
    elif tipo_sandwich == "2":
        print("Su sandwich " + str(sp[1]) + " ya esta preparado \n")
    elif tipo_sandwich == str(len(tipo_sandwich)) >= 3:
        print("Ya no nos queda stock de " + str(sp[2]) + "\n")
    elif tipo_sandwich == "3":
        print("Su sandwich " + str(sp[2]) + " ya esta preparado \n")
    elif tipo_sandwich == "4":
        print("Su sandwich " + str(sp[3]) + " ya esta preparado \n")
    elif tipo_sandwich == "5":
        print("Su sandwich " + str(sp[4]) + " ya esta preparado \n")
    else:  
        tipo_sandwich == "salir"
        sandwiches_terminados = sandwiches_terminados + 1
        print("¡Gracias por su compra!")
        break

sandwiches_terminados = str(len(tipo_sandwich))
print(sandwiches_terminados)