""" 
En este archivo vamos a trabajar con
Tuplas. tuple()
Las tuplas No son mutables
"""
numeros = (12, 99, 3.4, 'a', True, 99, False)
print(numeros)
# INDEX:
print(numeros[0])
# SLICING:
print(numeros[0:3])
print('numeros.index(3.4):')
print(numeros.index(3.4))
print('numeros.count(99):')
print(numeros.count(99))
print('type(numeros):')
print(type(numeros))
print('Diferencia entre list y tuple:')
print(f'list(numeros) = {list(numeros)}')
print(numeros)
numeros = list(numeros)
numeros[4] = 200
numeros = tuple(numeros)
print(numeros)
print()
""" 
En esta parte vamos a hablar de 
los conjuntos. set() 
No permiten repetidos
"""
print("CONJUNTOS:")
conjunto = {12, 3.4, 1, 99, 1, 2, 1}
print(conjunto)
A = {1, 3, 5, 7, 9}
print(f'A = {A}')
B = {2, 4, 6, 8, 10}
print(f'B = {B}')
print('A.union(B):')
print(A.union(B))
print()
print(f'conjunto = {conjunto}')
conjunto = list(conjunto)
conjunto[0] = 200
conjunto = set(conjunto)
print(f'conjunto = {conjunto}')
