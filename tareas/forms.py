from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Proyecto, Tarea

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion"]

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "descripcion", "estado"]