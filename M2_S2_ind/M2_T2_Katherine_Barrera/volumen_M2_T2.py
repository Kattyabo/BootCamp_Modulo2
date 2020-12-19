# a) ¿Cuál es el volumen de una esfera de radio 5?


def volumen_esfera(radio_esfera, constante_pi):
    volumen_esfera = 4/3 * constante_pi * radio_esfera**3
    return volumen_esfera

radio_esfera = 5
PI = 3.141592

vol_esf = volumen_esfera(radio_esfera, PI)

print("el resultado del volumen de la esfera es: " + str(vol_esf))