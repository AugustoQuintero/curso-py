""" 
En este archivo vamos a hacer
ejercicios. Ejercicio 1
"""
# CONTADOR DE PALABRAS.
entrada = input('Ingrese la frase: ').lower()
palabras = entrada.split(' ')
conjunto = list(set(palabras))
conjunto.sort()
print()
# print(conjunto[0])
# print(palabras.count(conjunto[0]))
# print(conjunto[1])
# print(palabras.count(conjunto[1]))
# print(conjunto[2])
# print(palabras.count(conjunto[2]))
salida = {}
for i in range(len(conjunto)):
    print(conjunto[i])
    print(palabras.count(conjunto[i]))
    salida[conjunto[i]] = palabras.count(conjunto[i])
print()
# salida = {'manzana': 2, 'banana': 2, 'melon': 1}
print(salida)

