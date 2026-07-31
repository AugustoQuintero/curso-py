""" 
En este archivo vamos a continuar trabajando
la estructura de control 
condicional: IF con elif.
"""
# SI el número que ingresa el ususario es
# negativo, se imprimen las líneas 5 y 6.
# positivo y menor a 10 se imprimen las líneas 7 y 8
# positivo y mayor o igual a 10 se imprimen 9 y 10
num = float(input('Ingrese número: '))
print('Línea 2')
print('Línea 3')
print('Línea 4')
if num < 0:
    print('Línea 5')
elif num >= 0 and num < 10:
    print('Línea 6')
elif num >= 10 and num < 100:
    print('Línea 7')
elif num >= 100 and num < 1000:
    print('Línea 8')
else:
    print('Línea 9')
    print('Línea 10')










