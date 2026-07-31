""" 
En este archivo vamos a trabajar con
los diccionarios. dict()
"""
clientes = {'Nombre': ['Juan', 'Pedro', 'Alberto', 'Diana'], 
            'Tel': [123, 456, 789, 987]}
print(clientes)
print()
print('clientes.keys():')
print(clientes.keys())
print()
print('list(clientes.keys():)')
print(list(clientes.keys()))
claves = list(clientes.keys())
print()
print('claves = list(clientes.keys())')
print(claves[0])
print()
print('list(clientes.values():)')
print(list(clientes.values()))
print()
valores = list(clientes.values())
print(valores[0])
print(valores[0][1])
print()
print(f'{valores[0][0]}\t{valores[1][0]}')
print(f'{valores[0][1]}\t{valores[1][1]}')
print(f'{valores[0][2]}\t{valores[1][2]}')
print(f'{valores[0][3]}\t{valores[1][3]}')
print()
c = 0
# f = 0,1,2,3
for f in range(4):
    print(f'{valores[0][f]}\t{valores[1][f]}')
print('Ejemplo:')
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royce', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004', '2024', '2014', '1997', '2009', '2015']}
print()
print(proveedores)
claves = list(proveedores.keys())
valores = list(proveedores.values())
print()
print(f'{claves[0]}\t{claves[1]}\t{claves[2]}')
for f in range(6):
    print(f'{valores[0][f]}\t{valores[1][f]}\t{valores[2][f]}')
print()




