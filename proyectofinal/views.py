from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def about(request):
    plantilla=loader.get_template('registroanimales/about.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def pages(request):
    plantilla=loader.get_template('registroanimales/pages.html')
    documento=plantilla.render()
    return HttpResponse(documento)

