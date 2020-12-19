# -*- coding: utf-8 *-* 

import bs4
import requests
import M2_T2_Katherine_Barrera.corrida_M2_T2

#tiempo recorrido en base a velocidad y distancia
salida_casa = float(input("Favor ingrese hora de salida, con separador de punto: "))
distancia1_suave = int(input("Favor ingrese la distancia recorrida, en km: "))
velocidad1_suave = int(input("Favor ingrese la velocidad recorrida, en km/hr: "))

#sólo se pueden importar constantes
suma_tiempo_hr = (distancia1_suave/velocidad1_suave)
llega = (suma_tiempo_hr + salida_casa)

#impresión resultados
print("LLega a la casa a las: " + str(llega) + " horas")
print("Demorándose en el trayecto: " + str(suma_tiempo_hr) + " horas")