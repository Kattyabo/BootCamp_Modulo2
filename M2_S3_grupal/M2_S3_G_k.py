import time
import datetime

# Escriba un programa que pregunte al usuario la hora del día.
# El usuario debe responder con un string en formaro hh:mm.

print("¡Hola!") 
time.sleep(1)
tiempo = str(input("Por favor me indicas la hora (hh:mm): "))

# El programa debe convertir la hora a número de segundos desde las
### 00:00 horas e imprimirlo en pantalla como por ejempolo “Han
### pasado 4000 segundos desde media noche”.

cadena = tiempo
separador = ":"
separado_por_dos_puntos = cadena.split(separador)

h = int(separado_por_dos_puntos[0])
m = int(separado_por_dos_puntos[1])
hh = h*3600
mm = m*60
t = hh+mm

print('\n' + "Gracias, han pasado: " + str(t) + " desde la media noche" + '\n')

# El programa debe además emitir un saludo diciendo:
### “Mañana” si la hora es mayor a las 06:00 y hasta las 12:00.
### “Tarde” si la hora es mayor a 12:00 y hasta las 17:00.
### “Atardecer” si la hora es mayor a 17:00 y hasta las 20:00.
### “Noche” si la hora es mayor a 20:00 y hasta las 02:00.
### “Madrugada” si la hora es mayor a 02:00 y hasta las 6:00.

if 6=< h <12:
    print ("Que tengas una buena Mañana") 
elif 12=< h <17:
    print ("Que tengas una buena Tarde")
elif 17=< h <20:
    print ("Que tengas un buen Atardecer")
elif 20 =< h:
    print ("Que tengas unas buenas Noches")
elif h =<2:
    print ("Que tengas unas buenas Noches")
else: 
    print ("Que tengas una buena Madrugada")

# Posteriormente el programa debe preguntar la fecha en formato
### DD:MM y el hemisferio en que se encuentra el usuario. En base a
### esto deberá indicar la estación del año en que se encuentra

time.sleep(1)
fecha = str(input("Por favor me indicas la fecha (dd:mm) "))
hemisferio = str(input("Por último, me indicas el hemisferio que te encuentras (norte-sur) "))

print(hemisferio)
cadena1 = fecha
separador1 = ":"
separado_por_puntos = cadena.split(separador1)

d = int(separado_por_puntos[0])
w = int(separado_por_puntos[1])

if hemisferio == sur and 4<= w =<12 and d>21:
    print ("Uff que calor! es Verano")
elif hemisferio == sur and 6>=w<=9 and d>21:  
    print ("Comenzando el frío y comienza el otoño")
elif hemisferio == sur and 9>=w<=12 and d>21:  
    print ("Hace mucho frío, es Invierno")
elif hemisferio == sur and 4>=w<=6 and d>21:  
    print ("Todo florece, ya es primavera")
elif hemisferio == norte and 4<=w=12 and d>21:  
    print ("Hace mucho frío, es Invierno")
elif hemisferio == norte and 6>=w<=9 and d>21:  
    print ("Todo florece, ya es primavera")
elif hemisferio == norte and 9>=w<=12 and d>21:  
    print ("Comenzando el frío y comienza el otoño")
else hemisferio == norte and 4>=w<=6 and d>21:  
    print ("Hace mucho frío, es Invierno")
