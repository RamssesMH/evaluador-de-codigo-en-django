from django.template import Template, Context
from modelo import models
from tareas.form import crearTareaForm
from django.shortcuts import render, redirect
import os
import subprocess

# Create your views here.
def subir_tarea(request):


    t = 'subir_tarea.html'
    alumno = models.Alumno.objects.get(usuario=request.session['user'])
    if request.method == "POST":
        
        # Fetching the form data
        uploadedFile = request.FILES["uploadedFile"]
        nombre = request.POST['nombreTarea']
        
                
        # Saving the information in the database
        document = models.Entregada(
                    
            usuario = alumno,
            nombre = nombre,
            uploadedFile = uploadedFile

        )
        document.save()
                
    documents = models.Tarea.objects.all()

    return render(request, t, context = {
    "files": documents
    })

def crear_dockerfile(id_tarea):
    path_comprobacion = models.Tarea.objects.get(id=id_tarea).script_comprobacion
    directorios = str(path_comprobacion).split('/')
    path = directorios[0]+"/"+directorios[1]
    file = path + "/Dockerfile"
    dockerfile = open(file, 'a+')
    dockerfile.write('FROM python:3.9\n')
    dockerfile.write('WORKDIR /usr/src/myapp\n')
    dockerfile.write('COPY . .\n')
    dockerfile.write('ENTRYPOINT ["python3"]\n')
    dockerfile.close()
    

def es_ejecucion_segura(id_tarea):
    path_comprobacion = models.Tarea.objects.get(id=id_tarea).script_comprobacion
    directorios = str(path_comprobacion).split('/')
    path = directorios[0]+"/"+directorios[1]
    file = path + "/Dockerfile"
    imagen = subprocess.Popen(['docker','build', path, '-t', 'python9'])




# Create your views here.

def crear_tarea(request):
    try:
        if request.session['Logueado'] == True:
            t = 'crear_tarea.html'
            form = crearTareaForm(request.POST)
            if request.method == 'GET':
                return render(request, t, { 'form': form })
            elif request.method == 'POST':
                print("entro post")
                if form.is_valid():
                    print("Entro form")
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
                    crear_dockerfile(tarea.id)
                    es_ejecucion_segura(tarea.id)
                    return redirect('/crearTarea/')
            
        else:
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')

def revisar_tarea(request):
    t = 'revisar_tarea.html'
    tareas_entregadas = models.Entregada.objects.all()
    return render(request, t, context = {
    "tareas": tareas_entregadas
    }) 
