from django.db import models

# Create your models here.
class Car(models.Model):
    titulo = models.TextField(max_length=250)
    
    