from django.shortcuts import render, redirect
from requests import request
# Create your views here.
def home(request):
    try:
        if request.session['Logueado'] == True:
            t = 'home.html'
            return render(request, t)
        else:
            return redirect('/')
    except Exception as e:
        return redirect('/')

