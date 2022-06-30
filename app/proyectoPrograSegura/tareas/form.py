from django import forms

class crearTareaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=400)
    