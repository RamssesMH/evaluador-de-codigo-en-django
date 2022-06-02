from email import message
from urllib.request import Request
from click import password_option
from django.template import RequestContext, Template, Context
from django.shortcuts import render, redirect
from matplotlib.style import context
from requests import request
from proyectoPrograSegura.form import LoginForm, TokenForm
import proyectoPrograSegura.settings as conf
from django.http import HttpResponse
from modelo import models
import datetime
from datetime import timezone
from tkinter.tix import MAIN
from pip import main
import requests
import sys
import crypt
import os
import base64
import re
import string
import random

def mandar_mensaje_bot(mensaje, token, chat_id):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + mensaje
    response = requests.get(send_text)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def  es_ip_conocida(ip: str):
    """
    Determina si la ip ya está en la BD
    keyword Arguments:
        ip: str
        returns: Boolean
    """
    registros = models.Peticion.objects.filter(ip=ip)
    return len(registros) != 0

def guardar_peticion(ip: str, intentos: int):
    """
    Rutina para almacenar información de petición, considerando las reglas de bloqueo de peticiones.

    Keyword Arguments:
    ip: str
    intentos: int, es el valor a guardar de intentos
    returns: None
    """
    fecha_actual = datetime.datetime.now(timezone.utc)
    if not es_ip_conocida(ip):
        entrada = models.Peticion(ip=ip, intentos=1,
                                  timestamp=fecha_actual)
        entrada.save()
        return
    registro = models.Peticion.objects.get(ip=ip)
    registro.intentos = intentos
    registro.timestamp = fecha_actual
    registro.save()

def esta_tiempo_en_ventana(timestamp):
    """
    Compara una fecha con la fecha actual
    keyword Arguments:
        timestamp: datetime de referencia
        returns: Bool
    """
    momento_actual = datetime.datetime.now(timezone.utc)
    resta = momento_actual - timestamp
    if resta.seconds < conf.VENTANA_SEGUNDOS_INTENTOS_PETICION:
        return True
    return False

def puede_hacer_peticion(ip):
    """
    Verdadero si la IP no ha alcanzado el límite de intentos.

    Keyword Arguments:
    ip --
    returns: Bool
    """
    if not es_ip_conocida(ip):
        guardar_peticion(ip, 1)
        return True
    registro = models.Peticion.objects.get(ip=ip)
    if not esta_tiempo_en_ventana(registro.timestamp):
        guardar_peticion(ip, 1)
        return True
    else:
        if (registro.intentos + 1) > conf.INTENTOS_MAXIMOS_PETICION:
            guardar_peticion(ip, registro.intentos + 1)
            return False
        else:
            guardar_peticion(ip, registro.intentos + 1)
            return True

def es_usuario_registrado(username, password_usuario):
    """
    Verdadero si el usuario está registrado y la contraseña es correcta

    Keyword Arguments:
    username: String
    password: String|
    returns: Bool
    """
    try:
        user = models.registro_usuarios.objects.filter(usuario=username).get()
        if user:
            password = user.password
            salt = password.split('$')[2]
            hasheado_p_usuario = crypt.crypt(password_usuario, '$6$' + salt)
            if user.password == hasheado_p_usuario:
                return True
            else:
                return False
    except Exception as e:
        return False

def get_token(username):
    """
    Crea token de acuerdo a la fecha en que se hace la petición
    keyword Arguments:
        timestamp: datetime de referencia
        returns: Bool
    """
    try:
        usuario = models.registro_usuarios.objects.filter(usuario=username).get()
        number_of_strings = 1
        length_of_string = 5
        for x in range(number_of_strings):
            digitos = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        timestamp = datetime.datetime.now(timezone.utc)
        token = models.token_login(token=digitos, id_usuario=usuario.id, timestamp=timestamp)
        token.save()
        return digitos
    except Exception as e:
        return None

def es_token_valido(username, password, token):
    """
    Compara si el token es valido de acuerdo a un tiempo de 3 minutos
    keyword Arguments:
        username
        token: frase de token alamacenada para cada nuevo login
        returns: Bool
    """
    print('entro a validacion de token')
    if es_usuario_registrado(username, password) == True:
        try:
            user = models.registro_usuarios.objects.filter(usuario=username).get()
            token = models.token_login.objects.filter(id_usuario=user.id).get()
            momento_actual = datetime.datetime.now(timezone.utc)
            resta = momento_actual - token.timestamp
            if resta.seconds < conf.INTENTOS_TOKEN_SEGUNDOS:
                if token == token.token:
                    return True
            return False
        except Exception as e: 
            return False

def enviar_formulario(request):
    """
    Login con número de intentos
    keyword Arguments:
        request --
        returns: HTTP_Response
    """
    message = None
    print('ENtro envio')
    t = 'envio.html'
    form = LoginForm(request.POST)
    token_request = 1
    if request.method == 'GET':
        return render(request, t, { 'message': message, 'form': form})
        
    elif request.method == 'POST':
        print('entro POST')
        try:
            tokenForm = TokenForm(request.POST, initial={ 'usuario': request.POST['usuario'], 'password': request.POST['password']})
            token_request = request.POST['token']
            print (token_request)
        except Exception as e:
            print (e)
            pass
        
        if token_request != 1:
            print('entro post TOKEN')
            print('entro en validForm')
            if tokenForm.is_valid():
                token = request.POST['token']
                if es_token_valido(username, password, token):
                    return HttpResponse('Logueado')
        else:
            if form.is_valid():
                username = request.POST['usuario']
                password = request.POST['password']
                if puede_hacer_peticion(get_client_ip(request)):
                    is_user = es_usuario_registrado(username, password)
                    if is_user is not False:
                        # login(request, user)
                        # tokenForm.fields['usuario'] = username
                        # tokenForm.fields['password'] = password
                        tokenF = get_token(username)
                        return render(request, 'token.html', { 'message': message, 'form': tokenForm} )
                        # request.session['logueado'] = True /l
                        # return HttpResponse('Logueado')
                        
                    else:
                        message = "Tu usuario y/o contraseña es incorrecto"
                else:
                    message = "Intentos agotados"
        return render(request, t, { 'message': message, 'form': form})
        

def validar_contraseña(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&-_]{10,}$"
    if re.search(regex, password) is not None:
        return True
    return False

def registro_usuarios(request):
    t = "registro.html"
    bytes_aleatorios = os.urandom(16)
    salt = base64.b64encode(bytes_aleatorios).decode('utf-8')
    if request.method == "GET":
        return render(request, t)
    elif request.method == "POST":
        usuario=request.POST.get('usuario', '')
        password=request.POST.get('password', '')
        if usuario == "":
            return HttpResponse("Todos los campos son requeridos")
        if password == "":
            return HttpResponse("Todos los campos son requeridos")
        if validar_contraseña(password) == False:
            return HttpResponse("Debe ingresar minimo 10 caracteres, una mayúscula, una minúscula, un digito y un caracter especial")
        hasheado = crypt.crypt(password, '$6$' + salt)
        registro_user=models.registro_usuarios(usuario=usuario, password=hasheado)
        registro_user.save()
        return render(request, t)
    


