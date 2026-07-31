""" 
Archivo de ejercicios resueltos
"""

# Realice un programa que 
# de un saludo personalizado
''' 
nombre = input()
print(f'Bienvenido {nombre}')
'''

# Realice un programa que 
# pida al usuario un número
# y diga si es par o impar
'''
numero = int(input("Ingrese número")) 
if numero % 2 == 0:
    print('Es par')
else:
    print('Es impar')
'''

# Realice un programa que 
# haga un conteo del uno
# al diez
'''
for i in range(1, 11):
    print(i)
'''

# Que el usuario adivine 
# el número
'''
num1 = 5
numero = int(input('Ingrese número: '))
if numero == num1:
    print('Correcto')
else:
    print('Te equivocaste')
'''

# Programa que suma los 5
# valores que ingrese el usuario
'''
suma = 0
for i in range(5):
    num = int(input(f'Ingrese número {i + 1}: '))
    suma = suma + num
print(f'el resultado es {suma}')
'''

# Realizar un contador de 10 a 1
'''
for i in range(10, 0, -1):
    print(i)
'''

# Triángulo de asteriscos
for i in range(5, 0, -1):
    print('*' * i)


















