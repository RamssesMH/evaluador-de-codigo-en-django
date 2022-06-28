from enum import unique
from django.db import models

# Create your models here.
class Peticion(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    intentos = models.IntegerField(default=1)
    timestamp = models.DateTimeField()

class registro_usuarios(models.Model):
    usuario = models.CharField(max_length=20, default="", unique=True)
    password = models.CharField(max_length=128, default="")
    token_telegram = models.CharField(max_length=50, default="")
    chat_id = models.CharField(max_length=20, default="")

class token_login(models.Model):
    token = models.CharField(max_length=5, unique=True)
    id_usuario = models.BigIntegerField()
    timestamp = models.DateTimeField()

class tarea(models.Model):
    nombre = models.CharField(max_length=40)
    id_usuario = models.BigIntegerField()
    id_grupo = models.BigIntegerField()

class grupo(models.Model):
    nombre = models.CharField(max_length=50)

class entregadas(models.Model):
    id_usuario = models.BigIntegerField()
    calificacion = models.IntegerField()