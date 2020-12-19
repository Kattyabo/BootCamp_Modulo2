'''b) Suponga que el precio de lista de un libro es de usd$ 24.95, pero las
librerías obtienen un 40% descuento (Más de 10 libros). El envío
cuesta usd$ 3 por la primera copia y usd$0.75 centavos por cada
copia adicional. ¿Cuál es el costo total al por mayor de 60 copias?
¿Cuál es el costo al por mejor de 5 copias?'''

precio1_libro = 24.95
descuento_libros = 1 - 0.4
costo1_envio = 3
costo_envio_ad = 0.75
libros_comprados = int(input("Favor ingrese el número de libros a comprar: "))


if libros_comprados <= 10:
    costo1_libros = libros_comprados * precio1_libro
    costo1_despacho = costo1_envio + (1 - libros_comprados) * costo_envio_ad
    total1_a_pagar = costo1_libros + costo1_despacho
    print("El costo total es: " + str(total1_a_pagar))
else:
    costo2_libros = libros_comprados * precio1_libro * descuento_libros
    costo2_despacho = costo1_envio + (libros_comprados - 1) * costo_envio_ad
    total2_a_pagar = costo2_libros + costo2_despacho + costo1_envio
    print("El costo total es: " + str(total2_a_pagar))
