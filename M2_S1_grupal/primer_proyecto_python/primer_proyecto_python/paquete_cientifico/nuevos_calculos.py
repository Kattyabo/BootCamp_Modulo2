import primer_script

# Restricciones: el radio debe ser mayor que cero

# a) Área y perímetro de círculo, dado su radio

radio = int(input("Ingresa el valor del radio: "))
area_circulo = (radio ** 2) * primer_script.PI
perimetro_circulo = (2 * primer_script.PI) / radio
print ("El area del círculo es: " + str(area_circulo))
print ("El perímetro del círculo es: " + str(perimetro_circulo))

# b) Área y perímetro de triangulo rectángulo, dadas su base y su altura.

altura_triangulo = int(input("ingresa el valor de la altura: "))
base_triangulo = int(input("ingresa el valor de la base: "))
c_triangulo = int(input("Ingresa el valor de la hipotenusa: "))
area_triangulo = ((altura_triangulo * base_triangulo) / 2)
perimetro_triangulo = (altura_triangulo + base_triangulo + c_triangulo)
print ("el área del triangulo rectángulo es: " + str(area_triangulo))
print ("El perimetro del triángulo es: "+ str(perimetro_triangulo))

# c) Área y perímetro de Rectándulo, dados sus lados.

altura_rectangulo = int(input("ingresa altura del rectángulo: "))
base_rectangulo = int(input("ingrese base del rectángulo: "))
area_rectangulo = (altura_rectangulo * base_rectangulo)
perimetro_rectangulo = ((base_rectangulo + altura_rectangulo) * 2)
print ("El área del rectángulo es: "+ str(area_rectangulo))
print (" el perímetro del rectángulo es: " + str(perimetro_rectangulo))

# Distancia recorrida, dados tiempo y velocidad.

velocidad1 = int(input("ingrese la velocidad: "))
tiempo1 = int(input("Ingrese el tiempo: "))
distancia_recorrida = (velocidad1 * tiempo1)
print("la distancia es: " + str(distancia_recorrida))

# La sentencia " if __name__ == "__main__": " --> 

## Nos permite conocer si el módulo ha sido ejecutado directamente o ha sido importado. 
## En resumen, permite que ejecute sólo valores del archivo original, no importados. 

if __name__ == "__main__":
    # area y perimeto de un circulo
    radio = 7
    print('El area del circulo: ' + str(area_circulo))
    print('El perimetro del circulo: ' + str(perimetro_circulo))

    # ·area y perimetro de un triangulo dados su base y altura
    base_triangulo = 9
    altura_triangulo = 12
    print('El area del triangulo es: ' + str(area_triangulo))
    print('El perimetro del triangulo es: ' + str(perimetro_triangulo))

    # area y perimetro de un rectangulo dados sus lados
    base_rectangulo = 10
    altura_rectangulo = 5
    print('El area del rectangulo es: ' + str(area_rectangulo))
    print('El perimetro del rectangulo es: ' + str (perimetro_rectangulo))

    tiempo1 = 10
    velocidad1 = 180
    print("La distancia recorrida es : " + str(distancia_recorrida) + " metros")
