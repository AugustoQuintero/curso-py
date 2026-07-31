""" 
Vamos a mirar algunas funciones
con los diccionarios.
"""
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royce', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004', '2024', '2014', '1997', '2009', '2015']}
print()
print(proveedores)
print()
print()
print(proveedores.get('Nombre'))
print(proveedores.get('Modelo'))
print()
print(proveedores.items())
print(proveedores['Nombre'])
print()
proveedores['Nombre'] = ['Mercedes', 'Ferrari', 'Porsche', 'Rolls Royce', 'BMW', 'Mustang']
print(proveedores)
proveedores.update({'Nombre': ['Mercedes', 'Ferrari', 'Porsche', 'Rolls Royce', 'BMW', 'Mustang']})
proveedores.pop('Precios')
print()
print(proveedores)
proveedores.popitem()
print()
print(proveedores)
proveedores['Propietarios'] = ['Yo', 'Tu', 'Él', 'Nosotros', 'Ustedes', 'Ella']
print()
print(proveedores)
prov2 = proveedores
prov2['Color'] = ['Az', 'Ng', 'Rj', 'Vd', 'Rs', 'Bl']
print()
print(prov2)
print()
print(proveedores)
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royce', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004', '2024', '2014', '1997', '2009', '2015']}
prov2 = proveedores.copy()
prov2['Color'] = ['Az', 'Ng', 'Rj', 'Vd', 'Rs', 'Bl']
print()
print(prov2)
print()
print(proveedores)
print('*' * 20)
print()
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royce', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004', '2024', '2014', '1997', '2009', '2015']}
print(proveedores)
proveedores['Nombre'][1] = 'Ferrari'
print()
print(proveedores)

