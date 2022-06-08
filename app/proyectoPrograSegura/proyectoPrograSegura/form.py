from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class TokenForm(forms.Form):
    token = forms.CharField(required=True,widget=forms.PasswordInput())

class RegistroForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    token_telegram = forms.CharField()
    id_chat = forms.CharField()