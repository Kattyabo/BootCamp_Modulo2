# a) Cálculo de VAN, es un procedimiento que permite calcular el valor
## el valor presente de un determinado número de flujos de caja futuros,
## originados por una inversión. A 5 años en el caso.

Inver_inicial = int(input("Ingrese Inversión inicial: "))
Flujo_neto1 = int(input("Ingrese flujo neto Año 1: "))
Flujo_neto2 = int(input("Ingrese flujo neto Año 2: "))
Flujo_neto3 = int(input("Ingrese flujo neto Año 3: "))
Flujo_neto4 = int(input("Ingrese flujo neto Año 4: "))
Flujo_neto5 = int(input("Ingrese flujo neto Año 5: "))
Tasa_ref = float(input("Ingrese tasa de referencia (habitualmente 0.15 en CORFO): "))
VAN = Inver_inicial + (Flujo_neto1/(1 + Tasa_ref)**1) + (Flujo_neto2/(1 + Tasa_ref)**2) + (Flujo_neto3/(1 + Tasa_ref)**3) + (Flujo_neto4/(1 + Tasa_ref)**4) + (Flujo_neto5/(1 + Tasa_ref)**5)
print ("El resultado de la VAN es: " + str(VAN))
