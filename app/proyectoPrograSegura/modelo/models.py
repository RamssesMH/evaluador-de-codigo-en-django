from enum import unique
from django.db import models
# def obtener_grupo():
#     grupo = Grupo.objects.get(id=1)
#     return grupo
# Create your models here.
class Peticion(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    intentos = models.IntegerField(default=1)
    timestamp = models.DateTimeField()
class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
class registro_usuarios(models.Model):
    nombre = models.CharField(max_length=50, default="", blank=False, )
    apellidos = models.CharField(max_length=50, default="", blank=False)
    usuario = models.CharField(max_length=20, default="", unique=True)
    password = models.CharField(max_length=128, default="")
    token_telegram = models.CharField(max_length=50, default="")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default="")
    chat_id = models.CharField(max_length=20, default="")
    tipo_usuario = models.CharField(max_length=15, default="")

class Maestro(models.Model):
    nombre = models.CharField(max_length=50, default="", blank=False, )
    apellidos = models.CharField(max_length=50, default="", blank=False)
    usuario = models.CharField(max_length=20, default="", unique=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default="")
    password = models.CharField(max_length=128, default="")
    token_telegram = models.CharField(max_length=50, default="")
    chat_id = models.CharField(max_length=20, default="")

class Alumno(models.Model):
    nombre = models.CharField(max_length=50, default="", blank=False, )
    apellidos = models.CharField(max_length=50, default="", blank=False)
    usuario = models.CharField(max_length=20, default="", unique=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default="")
    password = models.CharField(max_length=128, default="")
    token_telegram = models.CharField(max_length=50, default="")
    chat_id = models.CharField(max_length=20, default="")
    tipo_usuario = models.CharField(max_length=15, default="")
    
class token_login(models.Model):
    token = models.CharField(max_length=5, unique=True)
    id_usuario = models.BigIntegerField()
    timestamp = models.DateTimeField()

class Tarea(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400,default="")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default="")
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE, default="")



class Entregada(models.Model):
    usuario = models.ForeignKey(Alumno, on_delete=models.CASCADE, default="")
    calificacion = models.IntegerField()

    # 1237694558    5561606760:AAE6Bk1j4_vo-lvR_AZ--8jWz9TL2lo_zSA