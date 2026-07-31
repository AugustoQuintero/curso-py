from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.telefono}'
    


    