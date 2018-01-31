#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, RegModelForm
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


    return render(request, 'base.html', contexto)


def Contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

        form_email = form.cleaned_data.get('email')
        form_mensaje = form.cleaned_data.get('mensaje')
        form_nombre = form.cleaned_data.get('nombre')
        asunto = 'form de contacto'
        email_from = settings.EMAIL_HOST_USER
        email_mensaje = "%s: %s enviado por %s" %(form_nombre,form_email,form_mensaje) 
        email_to = [email_from,"otroemaill@gmail.com"] 
        send_mail(asunto, email_mensaje, email_from, email_to,
                  fail_silently=False)

        #print (email, mensaje, nombre)
    contexto = {'form': form}


    return render(request,"forms.html",contexto)