"""proyectoPrograSegura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import proyectoPrograSegura.views as vistas
import validadorCodigo.views as vistas_analizador
import tareas.views as vistas_tareas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistas.enviar_formulario),
    path('token/', vistas.enviar_token),
    path('registro/', vistas.registro_usuarios),
    path('logout/', vistas.logout),
    path('home/', vistas_analizador.home),
    #path('grupo/', vistas.crear_grupo),
    path('subir_tarea/', vistas_tareas.subir_tarea),
    path('crearTarea/', vistas_tareas.crear_tarea),
    path('revisar_tarea/', vistas_tareas.revisar_tarea),
    
]
