""" 
En este archivo vamos a trabajar con 
programación con clases
"""
class Persona:
    # Atributos.
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
    # Funciones.
    def hablar(self):
        print('Hola estimados amigos.')

class Estudiante(Persona):
    def __init__(self, nombre, documento, codigo):
        super().__init__(nombre, documento)
        self.codigo = codigo
    def monitor(self):
        print('Soy un monitor.')
    
def fun():
    pass

if __name__ == '__main__':
    ciudadano1 = Persona('David', 12345)
    print(ciudadano1.nombre)
    print(ciudadano1.documento)
    ciudadano1.hablar()

    ciudadano2 = Persona('Ivan', 98765)
    print(ciudadano2.nombre)
    print()
    estudiante1 = Estudiante('Diana', 1357, 1000)
    print(estudiante1.nombre)
    print(estudiante1.codigo)
    estudiante1.monitor()


