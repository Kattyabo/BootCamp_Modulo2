# 1) Escriba un programa que lea números desde el usuario a través de
## consola, y los agregue a una lista. No deben haber números duplicados en
## la lista. Si el usuario intenta agregar un número que ya está en la lista,
## imprima un mensaje de error corto y vuelva a solicitar un número distinto.
## Una vez que la lista contenga 15 números, el programa debe dejar de
## solicitar e imprimir el contenido de la lista.

listanum = []

alreadyExist = float(sum(list(map(lambda x: 1 if (x==numero) else 0,listanum))))

alreadyExist = 0

while len(listanum) <15:
    numero = float(input("Favor ingresar una lista aleatoria de números: "))
    for numero2 in listanum:
        if numero2 == numero:
            alreadyExist = 1
            break
        else:
            alreadyExist = 0
    if alreadyExist == 1:
        print("Éste número ya fué ingresado, intente nuevamente")
    else:
        listanum.append(numero)
       
print("La lista contiene:\n" + str(listanum) + "\n")

# 2) A continuación, escriba un programa que utilice un algoritmo el
## siguiente algoritmo para calcular los números primos hasta 500. Su
## programa debe comenzar creando una lista de números del 2 al 500 (¡No
## escriba manualmente la lista de los 500 números!). debe eliminar todos
## los múltiplos de 2 de la lista, sin incluir 2 (por lo que debe eliminar 4, 6, 8,
## 10, etc., pero no debe eliminar 2). Utilice la función remove(). Debería
## hacer lo mismo para 3, 4, 5, etc., hasta 25. Una vez hecho esto, debe
## imprimir los valores que aún están en la lista (¡todos deben ser números
## primos, ya que hemos eliminado todos los múltiplos!)

print("Ahora enlistaremos los números primos")
primos = []
p = 2

while p <= 500:

    primos.append(p)
    for h in range(2, p):

            if p%h==0:
                primos.remove(p)
                break
    p += 1

print("Los números primos del 1 al 500 son: \n") 
print(primos)
