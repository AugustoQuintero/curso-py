""" 
En este archivo vamos 
a realizar operaciones 
de comparación y lógicas:
"""
True
False
# Operaciones de comparación: < <= > >= == !=
num1 = 10
num2 = 20
print(f'num1 < num2: {num1 < num2}')
print(f'num1 <= num2: {num1 <= num2}')
print(f'num1 > num2: {num1 > num2}')
print(f'num1 >= num2: {num1 >= num2}')
print(f'num1 == num2: {num1 == num2}')
print(f'num1 != num2: {num1 != num2}')

# Operaciones lógicas: AND (y) OR (o) NOT (no)
print('\nOperaciones lógicas: AND')
2+3 == 9 and 4*5 < 1
print(f'False and False: {False and False}')
print(f'False and True: {False and True}')
print(f'True and False: {True and False}')
print(f'True and True: {True and True}')

print('\nOperaciones lógicas: OR')
2+3 == 9 or 4*5 < 1
print(f'False or False: {False or False}')
print(f'False or True: {False or True}')
print(f'True or False: {True or False}')
print(f'True or True: {True or True}')


print('\nOperaciones lógicas: NOT')
not 2+3 == 9
print(f'not False: {not False}')
print(f'not True: {not True}')

print('\nEjemplo:')
num1 = 80
num2 = 20
print('not (num1 >= num2 and num1 < 50')
print(not (num1 >= num2 and num1 < 50))

