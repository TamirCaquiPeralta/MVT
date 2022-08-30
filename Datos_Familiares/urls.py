from django.contrib import admin
from django.urls import path
from Datos_Familiares.views import Datos_Familiares
urlpatterns = [
    path('',Datos_Familiares),   
]
