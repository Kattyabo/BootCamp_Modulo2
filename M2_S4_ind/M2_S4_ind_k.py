# 1) Ingredientes para pizza:
## Escriba un loop que solicite al usuario ingresar una serie de ingredientes
## para pizzas hasta que ingresen el valor ‘quit’. A medida que el usuario
## agrega un ingrediente, imprima un mensaje que diga que agregará ese
## nombre de ingrediente a su pizza. Al ingresar la palabra ‘quit’ el programa
## revisará si se ingresó al menos 1 ingrediente. De lo contrario dira 
## ‘La pizza no es viable’.

ingredientes = []
contador_ing = 0
solicitud = str(input("Favor ingrese todos que desee en su pizza: \n"))

while solicitud != "quit":
    print("ingredientes: " + str(ingredientes))
    
    contador_ing = contador_ing + 1
    
    if contador_ing >= 1:
        break
print("ñam, su pizza es lista!" + str(ingredientes) + "\n")

# 2) Entradas de cine:
## Un cine cobra diferentes precios de entradas según la edad de una
## persona. Si una persona es menor de 3 años, la entrada es gratuita; si
## está entre 3 y 12 años el ticket cuesta $ $5.000; y si son mayores de 12
## años el ticket cuesta $7.000. Escriba un loop que pregunte a los usuarios
## su edad y luego informe el costo de su ticket de cine.

edad = 0
tarifa = 0
entrada = "s"
contador_ent = 0

while entrada == "s":
    edad = int(input('Indique su edad: \n'))
    if edad < 3 and edad <= 12:
        tarifa = 5000
    elif edad > 12:
        tarifa = 7000
    else:
        print("¡¡¡Entra Gratis!!!")
    print("Usted debe pagar: $ " + str(tarifa))

    contador_ent = contador_ent + 1
    if contador_ent >= cantidad_ent or contador_ent < 0:
        break
    entrada = input("¿Desea más entradas? s/n")
print("Gracias por su compra")











# 3) Tres salidas
## Escriba diferentes versiones de los ejercicios 1 y 2 con las siguientes variaciones:
#### a) Que utilice una prueba condicional en la instrucción while para
## detener el loop.
#### b) Que utilice una variable activa para controlar la duración máxima
## del loop.
#### c) Que utilice una instrucción break para salir del loop cuando el
## usuario ingrese un valor no esperado. Deberá entregar un mensaje
## apropiado para entender la causa del término del programa.

