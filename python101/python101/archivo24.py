""" 
En este archivo vamos a hacer
ejercicios. Ejercicio 2
"""
# INGRESO DE PRODUCTOS.
import os

def crear_producto():
    producto = input('Ingrese el producto: ')
    if producto in inventario:
        A = input(f'El producto {producto} se actualizará. "s" para continuar.\n')
        if A == 's':
            precio = input('Ingrese precio de ese producto:')
            inventario.update({producto: precio})
        else:
            print('Entendido. La actualización no se realizará.')
        os.system('pause')
    else:
        precio = input('Ingrese precio de ese producto:')
        inventario[producto] = precio
    return inventario

def leer_producto(diccionario):
    prod = input('Ingrese producto que quiere conocer: ')
    if prod in diccionario:
        print(f'El precio es {diccionario[prod]}')
    else:
        print('El producto no se encuentra en el inventario.')
    os.system('pause')
    
def borrar_producto():
    producto = input('Cuál es el producto que desea borrar? ')
    inventario.pop(producto)

inventario = {}
while True:
    os.system('cls')
    seleccion = input('\tMENÚ DE OPCIONES:\n1) Para crear o actualizar producto.\n2) Para saber precio de producto.\n3) Para borrar producto.\n4) Para salir.\n')
    if seleccion == '1':
        inventario = crear_producto()
    elif seleccion == '2':
        leer_producto(inventario)
    elif seleccion == '3':
        borrar_producto()
    else:
        print('Salimos.\n')
        break

print(inventario)


