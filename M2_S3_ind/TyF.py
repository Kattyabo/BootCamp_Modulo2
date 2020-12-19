import time

# 1) Escriba un programa que imprima en pantalla pruebas condicionales
# entre dos operandos. Y solicite al usuario predecir con t si es True o f
# si e False.

# 2) Luego de recibida la respuesta del usuario, el programa debe
# evaluar el resultado real e informar al usuario si su respuesta fué
# correcta o errada.

# 3) El programa debe realizar al menos 25 preguntas incluyendo:
#### Pruebas de igualdad y desigualdad con strings.
### Pruebas con la función lower().
### Pruebas numéricas que involucran igualdad y desigualdad, mayor
##### que y menor que, mayor o igual que, y menor o igual que.
### Pruebas con la palabra clave and y la palabra clave or.
### Prueba si un elemento está en una lista.
### Prueba si un elemento no está en una lista.

# 4) Dibuje un diagrama de flujo que represente este ejercicio.

'''SALUDO'''
print("¡Hola!\n")

pregunta1 = str(input("¿¿Estas de ánimo de responder unas divertidas preguntas??\n" + "T = True    F = False\n"))

if pregunta1 == "T" or pregunta1 == "t":
    print("!!!Que entretenido!!! A jugar...")
    time.sleep(2)    

else: 
    print("Hasta la próxima")


'''Calculadora:'''
print("Comencemos con algunos cálculos")

opcion = str(input("Selecciona una opción a trabajar: a . Suma, b . Resta, c . Multiplicación, d . División: "))

numero1 = int(input("ingrese el primer número: "))
numero2 = int(input("ingrese el segundo número: "))

if opcion == "a":
    resultado = numero1 + numero2
    print(resultado)

elif opcion == "b":
    resultado = numero1 - numero2
    print(resultado)

elif opcion == "c":
    resultado = numero1 * numero2
    print(resultado)

elif opcion == "d":
    resultado = numero1 / numero2
    print(resultado)

else: print("Opción no válida")


'''Mezcla de colores:'''
print("Ahora mezclaremos colores...")
print("  r. Rojo      a. Azul")

pregunta2 = input("  Elija un color (r o a): ")
if pregunta2 == "r":
    print("  a. Azul      v. Verde")
    pregunta3 = str(input("  Elija otro color (a o v): "))
        
    if pregunta3 == "a":
        print("La mezcla de Rojo y Azul produce Magenta.")
    else:
        print("La mezcla Rojo y Verde produce Amarillo.")
    
else:
    print("  v. Verde    r. Rojo")
    pregunta2 = str(input("  Elija otro color (v o r): "))
        
    if pregunta2 == "v":
        print("La mezcla de Azul y Verde produce Cian.")
    else:
        print("La mezcla Azul y Rojo produce Magenta.")
    
print("¡Hasta la próxima!")


'''Selección de trabajo por edad'''
print("Ahora necesitamos saber si tu edad te permite trabajar con nosotros")
edad = int(input("Por favor ingrese su edad: "))

if edad < 14:
    print("Eres un niño, no puedes trabajar")
elif edad >=15 and edad <17:
    print("Eres un adolecente, pero puedes trabajar con permiso de tus padres")
elif edad >=18 and edad <25:
    print("Eres joven, puedes trabajar, pero necesitas experiencia")
elif edad >=25 and edad <50:
    print("Eres Adulto, revisaremos tus antecedentes")
elif edad >=50 and edad <60:
    print("Eres muy mayor, estas a punto de jubilar")
elif edad >=60 and edad <99:
    print("Ya esta jubilado, no puede trabajar")
else:
    print("Ingrese un dato correcto")

time.sleep(3)

print("Muchas gracias por responder nuestras preguntas")
