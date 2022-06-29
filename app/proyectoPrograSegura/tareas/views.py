from django.template import Template, Context
from modelo import models
from django.shortcuts import render, redirect

# Create your views here.
def subir_tarea(request):
    t = 'subir_tarea.html'
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.tarea(
            nombre = fileTitle,
            uploadedFile = uploadedFile
            id_usuario = "3"
            id_grupo = "1"
        )
        document.save()

    documents = models.tarea.objects.all()

    return render(request, t, context = {
        "files": documents
    })