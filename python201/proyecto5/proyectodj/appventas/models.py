from django.db import models

# Create your models here.
class Carro(models.Model):
    titulito = models.TextField(max_length=200)
    anio = models.IntegerField(null=True)