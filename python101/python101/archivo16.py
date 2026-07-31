""" 
En este archivo vamos a
realizar funciones. 
palabra clave: DEF.
"""
def sumar(A=0, B=0):
    return A + B

def adicionar(A, B):
    print(f'La suma es {A + B}')

def bienvenida():
    print('Bienvenidos al curso de programación.')

def pi():
    return 3.141592

num1 = int(input('Ingrese primer número: '))
num2 = int(input('Ingrese segundo número: '))
num = sumar(num2)
print(f'La suma es {num}')
print('''Estamos simulando 
muchas líneas de 
ejecución''')
num1 = int(input('Ingrese primer número: '))
num2 = int(input('Ingrese segundo número: '))
adicionar(num1, num2)
print('Vamos a usar la función "bienvenida()":')
bienvenida()
print(f'EL valor de pi es: {pi()}')
