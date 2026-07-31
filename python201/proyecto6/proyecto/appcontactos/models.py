from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    detalle = models.TextField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.telefono} - {self.detalle}'