from django.db import models

# Create your models here.

class familiares (models.Model):
    Nombre = models.CharField(max_length=99)
    Apellido = models.CharField(max_length=99)
    Edad = models.IntegerField()
    Fecha_Nacimiento = models.DateField()
    