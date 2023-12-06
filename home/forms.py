from django import forms
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Ingrese su nombre de usuario"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"type":"password", "class":"form-control", "placeholder":"Ingrese su contraseña"}))

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Ingrese un nombre de usuario"}))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Escriba una contraseña "}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Confirmar contraseña"}))
    first_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escriba su primer nombre"}))
    last_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escriba su apellido paterno"}))
    email = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escriba su correo electronico"}))

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email"
        ]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        