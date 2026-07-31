"""  
En este archivo vamos a 
continuar con nuestro juego
en version 3.
"""
def igual(A, B):
    if A == B:
        return True
    return False

def menorque(A, B):
    if A < B:
        return True
    return False

def mayorque(A, B):
    if A > B:
        return True
    return False
    
import random
num1 = random.randint(1, 100)
while True:
    numero = int(input('Ingrese número: '))
    if igual(numero, num1):
        print('Correcto')
        break
    elif menorque(numero, num1):
        print('Digite un número mas grande. ')
    elif mayorque(numero, num1):
        print('Digite un número mas pequeño.')



