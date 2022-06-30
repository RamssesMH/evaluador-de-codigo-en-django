from django.template import Template, Context
from modelo import models
from tareas.form import crearTareaForm
from django.shortcuts import render, redirect

# Create your views here.
def subir_tarea(request):
    t = 'subir_tarea.html'
    usuario= request.session['user']
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
