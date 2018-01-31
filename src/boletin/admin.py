#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .forms import RegModelForm
from .models import Registrado

# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
    list_display =["email","nombre","timestamp"]
    form=RegModelForm
    #list_display_links=["nombre"]
    list_filter=["timestamp"]
    list_editable=["nombre"]
    search_fields=["email","nombre"]
    #class Meta:
       # model =Registrado



admin.site.register(Registrado,AdminRegistrado)