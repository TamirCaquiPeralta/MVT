from re import template
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Datos_Familiares.models import familiares
# Create your views here.

def Datos_Familiares(request):
    Familiar = familiares.objects.all()
    dic = {'Familiares':Familiar}
    template = loader.get_template('Template1.html')
    Document_HTML = template.render(dic)
    return HttpResponse(Document_HTML)
