from email import message
from django.shortcuts import render, redirect
from tareas.form import crearTareaForm
from datetime import datetime
from modelo import models
import subprocess
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs/app.log',
                    filemode='a')

def crear_dockerfile(path): 
    """
    Rutina que permite crear el archivo de configuración para crear una imagen de Docker
    keyword Arguments:
        path: string
        returns: None
    """
    file = path + "/Dockerfile"
    dockerfile = open(file, 'a+')
    dockerfile.write('FROM python:3.9\n')
    dockerfile.write('WORKDIR /usr/src/myapp\n')
    dockerfile.write('COPY . .\n')
    dockerfile.write('ENTRYPOINT ["python3"]\n')
    dockerfile.close()

def obtener_nombre_archivo(path):
    """
    Rutina que separa el nombre del archivo del directorio
    keyword Arguments:
        path: string
        returns: String
    """
    directorio_archivo = path.split('/')
    archivo = directorio_archivo[2]
    return archivo

def ejecutar_tarea(path, id_entrega, id_tarea):
    """
    Rutina que ejecuta una tarea en un ambiente controlado (sandbox)
    keyword Arguments:
        path: string
        nombre: string
        returns: Int (Calificación)
    """
    tarea = models.Tarea.objects.get(id=id_tarea)
    tarea_inicializacion = tarea.script_inicializacion
    tarea_comprobacion = tarea.script_comprobacion
    tarea_parametros = tarea.script_parametros
    script_inicializacion = obtener_nombre_archivo(str(tarea_inicializacion))
    script_comprobacion = obtener_nombre_archivo(str(tarea_comprobacion))
    script_parametros = obtener_nombre_archivo(str(tarea_parametros))
    script_alumno =  obtener_nombre_archivo(str(models.Entregada.objects.get(id=id_entrega).uploadedFile))
    nombre = str(id_entrega)+"-"+str(id_tarea)
    
    imagen = subprocess.run(['docker', 'build', path, '-t', nombre])
    iniciar = subprocess.run(['docker', 'run', '--name', nombre, nombre, 'main.py', '-i', script_inicializacion, '-p', script_parametros, '-c', script_comprobacion, '-a', script_alumno], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    borrar_contenedor = subprocess.run(['docker', 'rm', nombre])
    borrrar_imagen = subprocess.run(['docker', 'image', 'rm', nombre])
    out = iniciar.stdout.decode('utf-8')
    print (out)
    calif = out[-3:]
    c = calif.strip()
    c = int(c)
    return c
 
def subir_tarea(request):
    """
    Rutina que permite al estudiante responder a una tarea
    keyword Arguments:
        request --
        returns: HTTP_Redirect
    """
    if request.session['Logueado'] == True:
        if request.session['tipo_usuario'] == "alumno":
            t = 'subir_tarea.html'
            documents = models.Tarea.objects.all()
            alumno = models.Alumno.objects.get(usuario=request.session['user'])
            if request.method == 'GET':
                return render(request, t, context = {
                "files": documents
                })
            elif request.method == "POST":
                
                uploadedFile = request.FILES["uploadedFile"]
                nombre = request.POST['nombreTarea']
                tarea = models.Tarea.objects.get(id=nombre)
                document = models.Entregada(
                    usuario = alumno,
                    nombre = nombre,
                    uploadedFile = uploadedFile
                )
                document.save()
                documento = document.uploadedFile
                ruta = str(documento)
                ruta_ejers = models.Tarea.objects.get(id=document.nombre)
                ruta_ejer = ruta_ejers.script_comprobacion
                ruta_ejer = str(ruta_ejer)
                x = ruta.split('/')
                ruta_final = x[0].strip()+"/"+x[1].strip()+"/"
                x = ruta_ejer.split('/')
                ruta_final_ejer = x[0].strip()+"/"+x[1].strip()+"/"
                comando_completo= "cp "+ruta_final_ejer+"* "+ ruta_final
                crear_dockerfile(ruta_final)
                os.system(comando_completo)
                copiar_script_principal = "cp script_general/* " + ruta_final
                os.system(copiar_script_principal)
                nombre_imagen_docker = str(document.id)+"-"+str(document.nombre)
                calificacion = ejecutar_tarea(ruta_final, document.id, document.nombre)
                calif = models.Entregada.objects.get(id=document.id)
                calif.calificacion = calificacion
                calif.save()
                nombre_tarea = str(models.Tarea.objects.get(id=calif.nombre).nombre)
                message = "Tu calificación a la tarea "+ nombre_tarea +" es "+ str(calif.calificacion)
                logging.info(f'El usuario ha subido una tarea {calif.usuario}')
            return render(request, t, context = {
            "files": documents,
            'message': message
            })
        else:
            return redirect('/home')
    else:
        return redirect('/')

def crear_tarea(request):
    """
    Rutina que permite al maestro crear una Tarea
    keyword Arguments:
        request --
        returns: HTTP_Redirect
    """
    try:
        if request.session['Logueado'] == True:
            if request.session['tipo_usuario'] == "maestro":
                t = 'crear_tarea.html'
                form = crearTareaForm(request.POST)
                if request.method == 'GET':
                    return render(request, t, { 'form': form })
                elif request.method == 'POST':
                    if form.is_valid():
                        nombre = request.POST['nombre']
                        descripcion = request.POST['descripcion']
                        grupo = models.Grupo.objects.get(id=1)
                        maestro = models.Maestro.objects.get(usuario=request.session['user'])
                        script_comprobacion = request.FILES["script_comprobacion"]
                        script_parametros = request.FILES["script_parametros"]
                        script_inicializacion = request.FILES["script_inicializacion"]
                        tarea = models.Tarea(
                            nombre=nombre,
                            descripcion=descripcion,
                            grupo=grupo,
                            maestro=maestro,
                            script_comprobacion=script_comprobacion,
                            script_parametros=script_parametros,
                            script_inicializacion=script_inicializacion
                        )
                        tarea.save()
                        logging.info(f'El maestro {maestro} ha creado la tarea {tarea.nombre}')
                        return redirect('/crearTarea/')
            else:
                return redirect('/home')
        else:
            return redirect('/')
    except Exception as e:
        return redirect('/')

def revisar_tarea(request):
    """
    Rutina que permite a un maestro, ver todas las tareas calificadas
    keyword Arguments:
        request --
        returns: HTTP_Redirect
    """
    if request.session['Logueado'] == True:
        if request.session['tipo_usuario'] == "maestro":
            t = 'revisar_tarea.html'
            tareas_entregadas = models.Entregada.objects.all()
            alumno = models.Alumno.objects.all()
            return render(request, t, context = {
            "tareas": tareas_entregadas, "alumnos": alumno
            })
        else:
            return redirect('/home')
    else:
        return redirect('/home')
