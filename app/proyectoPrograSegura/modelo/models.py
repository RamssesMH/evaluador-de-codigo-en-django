from django.db import models
import datetime

def directorio_archivo(instance, archivo):
    tarea = str(instance.nombre).lower().replace(" ", "_").strip()
    fecha = datetime.date.today()
    nombre_directorio = tarea + str(fecha)
    return 'media/{0}/{1}'.format(nombre_directorio, archivo)

def directorio_tarea(instance, archivo):
    """ este es el numero de la actividad a la que se quiso responder"""
    tarea = str(instance.nombre)
    """Es la id del usuario que respondio la actividad"""
    tarea2 = str(instance.usuario_id)
    fecha = datetime.date.today()
    nombre_directorio = tarea+"-"+tarea2+"-" + str(fecha)
    return 'tarea-subida/{0}/{1}'.format(nombre_directorio, archivo)
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
    nombre = models.CharField(max_length=40,default="")
    descripcion = models.CharField(max_length=400,default="")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default="")
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE, default="")
    script_comprobacion = models.FileField(upload_to =directorio_archivo, default="")
    script_inicializacion = models.FileField(upload_to =directorio_archivo, default="")
    script_parametros = models.FileField(upload_to =directorio_archivo, default="")
class Entregada(models.Model):
    usuario = models.ForeignKey(Alumno, on_delete=models.CASCADE, default="")
    calificacion = models.IntegerField(default=00)
    nombre = models.CharField(max_length=40,default="")
    uploadedFile = models.FileField(upload_to=directorio_tarea,default="")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
