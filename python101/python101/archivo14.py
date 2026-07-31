""" 
En este archivo continuamos con 
nuestro juego de adivinar
un número
versión 2
"""
import random
num1 = random.randint(1, 100)
while True:
    numero = int(input('Ingrese número: '))
    if numero == num1:
        print('Correcto')
        break
    elif numero < num1:
        print('Digite un número mas grande. ')
    else:
        print('Digite un número mas pequeño.')

