""" 
En este archivo vamos a ver la
palabra reservada WHILE.
"""
'''
i = 0
while i < 5:
    print('Hola')
    i = int(input())
'''
'''
while True:
    print('Estoy en el WHILE.')
    variable = input('Digite "s" si quiere salir ')
    if variable == 's':
        break
print('Estoy fuera del WHILE.')
'''

variable = 'n'
while variable != 's':
    print('Estoy en el WHILE.')
    variable = input('Digite "s" si quiere salir ')
print('Estoy fuera del WHILE.')



