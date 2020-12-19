##c.-Si salgo de mi casa a las 6:52 am y corro 1km a un ritmo suave 
##(8km/hr), luego 3km a tirmo medio (15km/hr) y 1km a un ritmo suave
##(10km/hr) ¿A qué hora vuelvo a casa?

salida_casa = 6.52  #en formato float, se debe cambiar a minutos
salida_casa_hr = (6 * 60) + 52

distancia1_suave = 1 #km distancia
velocidad1_suave = 8 #km/hora velocidad
tiempo_suave_hr = distancia1_suave / velocidad1_suave

distancia_media = 3
velocidad_media = 15
tiempo_media_hr = distancia_media / velocidad_media

distancia2_suave = 1
velocidad2_suave = 10
tiempo2_suave_hr = distancia2_suave / velocidad2_suave

suma_tiempo_hr = (tiempo_suave_hr + tiempo_media_hr + tiempo2_suave_hr)*60
llega = ((suma_tiempo_hr) + salida_casa_hr) / 60 

print("LLega a la casa a las: " + str(llega) + " horas")
print("Demorándose en el trayecto: " + str(suma_tiempo_hr) + " minutos")
