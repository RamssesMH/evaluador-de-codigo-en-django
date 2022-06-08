from email import message
from django.template import RequestContext, Template, Context
from django.shortcuts import render, redirect
from requests import request
from proyectoPrograSegura.form import LoginForm, TokenForm, RegistroForm
import proyectoPrograSegura.settings as conf
from django.http import HttpResponse
from modelo import models
import datetime
from datetime import timezone
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
    usuario = models.registro_usuarios.objects.filter(usuario=username).get()
    try:
        tokenGet = models.token_login.objects.filter(id_usuario=usuario.id).get()
        tokenGet.delete()
    except Exception as e:
        pass
    number_of_strings = 1
    length_of_string = 5
    for x in range(number_of_strings):
        digitos = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    timestamp = datetime.datetime.now(timezone.utc)    
    token = models.token_login(token=digitos, id_usuario=usuario.id, timestamp=timestamp)
    token.save()
    mandar_mensaje_bot(token.token, usuario.token_telegram, usuario.chat_id)
    return digitos

def es_token_valido(username, token):
    """
    Compara si el token es valido de acuerdo a un tiempo de 3 minutos
    keyword Arguments:
        username
        token: frase de token alamacenada para cada nuevo login
        returns: Bool
    """
    print('entro a validacion de token')
    try:
        usuario = models.registro_usuarios.objects.filter(usuario=username).get()
        print(usuario.id)
        tokenGet = models.token_login.objects.filter(id_usuario=usuario.id).get()
        print(tokenGet)
        momento_actual = datetime.datetime.now(timezone.utc)
        resta = momento_actual - tokenGet.timestamp
        if resta.seconds < conf.INTENTOS_TOKEN_SEGUNDOS:
            print('entro comparacion de 3 minutos')
            if token == tokenGet.token:
                return True
        return False
    except Exception as e: 
        return False

def enviar_token(request):
    """
    Página con número de intentos
    keyword Arguments:
        request --
        returns: HTTP_Response
    """
    try:
        if request.session['access_token'] == True:
            message = 'El token se ha enviado a Telegram, es válido sólo por 3 minutos'
            t= 'envio.html'
            form = TokenForm(request.POST)
            if request.method == 'GET':
                return render(request, t, { 'message': message,'form':form })
            elif request.method == 'POST':
                if form.is_valid():
                    print('El formulario es válido')
                    token = request.POST['token']
                    username = request.session['user']
                    if es_token_valido(username, token):
                        request.session['access_token'] = False
                        request.session['Logueado'] = True
                        return redirect('/home/')
                    else:
                        request.session.flush()
                        return redirect('/')
        else: 
            return redirect('/home')
    except Exception as e:
        return redirect('/home')

def enviar_formulario(request):
    """
    Login con número de intentos
    keyword Arguments:
        request --
        returns: HTTP_Response
    """
    try:
        if request.session['Logueado'] == True:
            return redirect('/home')
    except Exception as e:
            
        request.session.flush()
        message = ''
        t = 'envio.html'
        form = LoginForm(request.POST)
        if request.method == 'GET':
            return render(request, t, { 'form': form })
            
        elif request.method == 'POST':
            if form.is_valid():
                username = request.POST['usuario']
                password = request.POST['password']
                if puede_hacer_peticion(get_client_ip(request)):
                    is_user = es_usuario_registrado(username, password)
                    if is_user is not False:
                        request.session['access_token'] = True
                        request.session['user'] = username
                        token = get_token(username)
                        return redirect('/token/')
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
    t = 'envio.html'
    form = RegistroForm(request.POST)
    if request.method == "GET":
        return render(request, t, {'form': form})
    elif request.method == "POST":
        usuario=request.POST['usuario']
        password=request.POST['password']
        token_telegram = request.POST['token_telegram']
        id_chat = request.POST['id_chat']
        if usuario == "":
            message = "Todos los campos son requeridos"
            return render(request, t, { 'message': message, 'form': form})
        if password == "":
            message = "Todos los campos son requeridos"
            return render(request, t, { 'message': message, 'form': form})
        if validar_contraseña(password) == False:
            message = "Debe ingresar minimo 10 caracteres, una mayúscula, una minúscula, un digito y un caracter especial"
            return render(request, t, { 'message': message, 'form': form})
        bytes_aleatorios = os.urandom(16)
        salt = base64.b64encode(bytes_aleatorios).decode('utf-8')
        hasheado = crypt.crypt(password, '$6$' + salt)
        registro_user=models.registro_usuarios(usuario=usuario, password=hasheado, token_telegram=token_telegram, chat_id=id_chat)
        registro_user.save()
        return redirect('/')
    


def logout(request):
    request.session['Logueado'] = False
    request.session['access_token'] = False
    request.session.flush()
    return redirect('/')

def home(request):
    try:
        if request.session['Logueado'] == True:
            t = 'home.html'
            return render(request, t)
        else:
            return redirect('/')
    except Exception as e:
        return redirect('/')