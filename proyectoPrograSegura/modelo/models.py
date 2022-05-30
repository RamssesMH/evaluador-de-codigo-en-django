from enum import unique
from django.db import models

# Create your models here.
class Peticion(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    intentos = models.IntegerField(default=1)
    timestamp = models.DateTimeField()

class registro_usuarios(models.Model):
    usuario = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=128, default="")