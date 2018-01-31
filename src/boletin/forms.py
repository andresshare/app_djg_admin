#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from .models import Registrado


class RegModelForm(forms.ModelForm):

    class Meta:

        model = Registrado
        fields = ['nombre', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base,proveeder =email.split("@")
        dominio,extension =proveeder.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Usar email con extension .edu")
        return email
    def Clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        #validaciones
        return nombre

class RegForm(forms.Form):

    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()



			