from click import password_option
from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class TokenForm(forms.Form):
    usuario = forms.CharField(disabled=True)
    password = forms.CharField(widget=forms.PasswordInput(), disabled=True)
    token = forms.CharField(required=True)
    