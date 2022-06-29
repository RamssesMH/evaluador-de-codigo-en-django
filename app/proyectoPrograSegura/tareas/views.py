from django.template import Template, Context
from modelo import models
from tareas.form import crearTareaForm
from django.shortcuts import render, redirect

# Create your views here.
def subir_tarea(request):
    t = 'subir_tarea.html'
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Tarea(
            nombre = fileTitle,
            uploadedFile = uploadedFile

        )
        document.save()

    documents = models.Tarea.objects.all()

    return render(request, t, context = {
        "files": documents
    })

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
                    maestro = models.Grupo.objects.get(usuario=request.session['user'])
                    print(request.session['user'])
                    tarea = models.Tarea(nombre=nombre, descripcion=descripcion, grupo=grupo, maestro=maestro)
                    print(tarea)
                    tarea.save()
                    return redirect('/crearTarea/')
            
        else:
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')
