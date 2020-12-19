# -*- coding: utf-8 -*-
import bs4
import requests
import paquete_cientifico as p

# x = requests.get('https://www.google.com')
# print(x.text)

print(p.PI)

area = 30
altura = 10

volumen = p.vol_cilindro(altura, area)
print("Volumen de Cilindro: "  + str(volumen))

multiplicacion = p.multiplica(30, 20)
print(multiplicacion)


print(dir(p))