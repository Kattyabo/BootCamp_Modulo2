x = 3                   
f = 3.1415926               
name = "Python"
print(x)
print(f)
print(nombre)
combination = nombre + " " + nombre
print(combinacion)
suma = f + f
print(suma)


# funcion retornara la raiz cuadrada de valor
def raiz_cuadrada(valor):
    raiz_cuadrada = valor**(0.5)
    return raiz_cuadrada


# convertir caracter a valor ASCII
def convertir_ascii(char):
    convertir_ascii = ord(char)
    return convertir_ascii


# convertir un numero a codigo ASCII
def convertir_num(num):
    convertir_num = chr(num)
    return convertir_num

# calculadora de porcentajes de una cantidad


def porcentaje_cantidad(porcentaje, cantidad):
    porcentaje_cantidad = porcentaje*cantidad/100
    return porcentaje_cantidad


# calcula la cantidad total dado un porcentaje
def cantidad_porcentaje(porcentaje, cantidad):
    total = porcentaje*cantidad/10
    return total


if __name__ == "__main__":
    # funcion raiz cuadrada de 16
    valor = 16
    print(raiz_cuadrada(valor))

    # funcion convertir un char a valor ASCII
    char = 'g'
    print(convertir_ascii(char))
    # funcion convertir un numero a codigo ASCII
    num = 103
    print(convertir_num(num))

    porcentaje = 10
    cantidad = 100
    print(str(porcentaje_cantidad(porcentaje, cantidad))+'%')
    print(cantidad_porcentaje(porcentaje, cantidad))