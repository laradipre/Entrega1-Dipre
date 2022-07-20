from unittest.util import _MAX_LENGTH
from django.db import models


class Supermercado(models.Model):
    sucursal = models.CharField(max_length=50)
    empleados = models.IntegerField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_de_caja = models.IntegerField()

class Cliente (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()



