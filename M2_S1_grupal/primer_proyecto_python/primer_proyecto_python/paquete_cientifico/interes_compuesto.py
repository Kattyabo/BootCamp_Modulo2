# a) Interés Compuesto: significa que el interés ganado sobre el capita
##invertido se añade al principal. Se gana interés sobre el interés.
##De otra forma se asume reinversión de los intereses obtenidosv en periodos intermedios.

Capitalc_a = int(input("Ingresa del capital: "))
TasaC_a = float(input("Ingresa tasa anual: "))
TiempoC_a = int(input("Ingresa tiempo en años: "))
Monto_final = Capitalc_a * (1 * TasaC_a) ** TiempoC_a
print ("El monto al finalizar el periodo es: " + str(Monto_final))
