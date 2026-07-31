""" 
En este archivo vamos a hablar 
sobre las listas. list()
Las listas son mutables.
"""
[32, 43, 54]
[32.4, 4.3, 5.4]
['Pedro', 'José', 'Juan']
[True, False, True]
[12, 1.78, 'Carlos', True]

print(type([32, 43, 54]))

print([12, 3.14, True, 'Carlos', [1, 2, 3.4, 'Hola']])

[[1,2],[3,4]]
print()
print('Lista de enteros:')
numeros = [32, 43, 54, 67]
print(numeros)
# INDEX:
print(numeros[0])
# SLICING:
print(numeros[0:3])
print(numeros[0:3:2])
print(numeros[1:])
print(numeros[::2])
numeros[1] = 99
print(numeros)
var = int(input('Ingrese nuevo valor: '))
numeros.append(var)
print(numeros)
numeros.insert(1, var)
print(numeros)
numeros.pop()
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(200)
print()
print('Con repeticiones:')
numeros = [32, 200, 43, 54, 200, 67]
print(numeros)
repetido = numeros.count(200)
pos = []
A = numeros.index(200)
pos.append(A)
A = numeros.index(200, A+1)
pos.append(A)
print(pos)
