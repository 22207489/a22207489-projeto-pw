from django.shortcuts import render

# Create your views here.

# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view2(request):
    return HttpResponse("Website criado com sucesso!")

def index_view3(request):
    return HttpResponse("O meu primeiro website em programação web")
