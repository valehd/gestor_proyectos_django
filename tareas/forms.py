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

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()

        if len(nombre) < 3:
            raise forms.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )

        return nombre

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "descripcion", "estado"]

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()

        if len(titulo) < 3:
            raise forms.ValidationError(
                "El título debe tener al menos 3 caracteres."
            )

        return titulo


    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"].strip()

        if len(descripcion) < 5:
            raise forms.ValidationError(
                "La descripción debe tener al menos 5 caracteres."
            )

        return descripcion

    