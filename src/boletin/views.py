#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from .forms import RegForm, RegModelForm
from .models import Registrado


# Create your views here.

def inicio(request):
    titulo = 'Hola'
    if request.user.is_authenticated:
        titulo = 'Bienvenido %s' %(request.user)

    form = RegModelForm(request.POST or None)

    contexto = {
        'titulo': titulo, 
        'el_form': form
        }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre=form.cleaned_data.get("nombre")
        email=form.cleaned_data.get("email")

        if not instance.nombre:
            instance.nombre ="Persona"
            instance.save()
            contexto = {
                'titulo': "Gracias %s!" %(nombre)
                }
        if not nombre:
            contexto={
                "titulo": "Gracias %s!"%(email)
            }
        print (instance)
        print (instance.timestamp)
        # form_data = form.cleaned_data
        # abc = form_data.get('email')
        # abc2 = form_data.get('nombre')
        # obj = Registrado.objects.create(email=abc, nombre=abc2)

        # obj=Registrado()
        # obj.email =abc
        # obj.save()

    

    return render(request, 'inicio.html', contexto)



			