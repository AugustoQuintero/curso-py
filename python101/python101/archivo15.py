""" 
En este archivo vamos a hablar de 
los 'IMPORT'
"""
'''
import math
print(math.sqrt(4))
'''
# Otra forma de importar:
from math import *
print(sqrt(4))
print(tan(4))
print(sin(4))
'''
'''
'''
# Para generar números aleatorios
import random
print(random.random())
print(random.random() * 100)
print(random.randint(1, 100))
'''
'''
import os
os.system("dir")
'''
'''
import datetime
print(datetime.time(1, 30))
'''
'''
import time
print('Iniciando programa...')
time.sleep(10)
print('Terminando programa...')
'''
'''
import time
import os
for i in range(10, 0, -1):
    time.sleep(1)
    os.system("cls")
    print(i)
time.sleep(1)
os.system("cls")
print("Despegue....")
'''

from datetime import datetime
fecha1 = datetime(2025, 6, 21)
anio = int(input('Ingrese año: '))
mes = int(input('Ingrese mes: '))
dia = int(input('Ingrese día: '))
fecha2 = datetime(anio, mes, dia)
diferencia = fecha2 - fecha1
print(f'Te faltan {diferencia.days} días para tu cumpleaños')









