from django import forms

class crearTareaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=400, required=True)
    