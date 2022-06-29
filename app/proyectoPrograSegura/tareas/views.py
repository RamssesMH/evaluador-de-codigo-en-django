from tareas.form import crearTareaForm
from django.shortcuts import render, redirect

from requests import request
from modelo import models

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
                    tarea = models.Tarea(nombre=nombre, descripcion=descripcion, grupo=grupo, maestro=maestro)
                    tarea.save()
                    return redirect('/crearTarea/')
            
        else:
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')