# a) Interés Simple que aplica por año

Capital_a = int(input("Ingresa del capital: "))
Tasa_a = float(input("Ingresa tasa anual: "))
Tiempo_a = int(input("Ingresa tiempo en años: "))
Interes_a = Capital_a * (Tasa_a / 100) * Tiempo_a
print ("El interés calculado es: " + str(Interes_a))

# b) Interés Simple que aplica por mes

Capital_m = int(input("Ingresa del capital: "))
Tasa_m = float(input("Ingresa tasa anual: "))
Tiempo_m = int(input("Ingresa tiempo en años: "))
Interes_m = Capital_m * (Tasa_m / 100) * (Tiempo_m / 12)
print ("El interés calculado es: " + str(Interes_m))

# c) Interés Simple que aplica por día

Capital_d = int(input("Ingresa del capital: "))
Tasa_d = float(input("Ingresa tasa anual: "))
Tiempo_d = int(input("Ingresa tiempo en años: "))
Interes_d = Capital_d * (Tasa_d / 100) * (Tiempo_d / 365)
print ("El interés calculado es: " + str(Interes_d))