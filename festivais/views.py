from django.shortcuts import render

from .models import Festival, Banda, Localizacao

def festivais_view(request):
    context = {
        'festivais': Festival.objects.all(),
        'localizacoes':Localizacao.objects.all(),
    }
    return render(request, "festivais/festivais.html", context)


def festival_view(request, festival_id):
    context = {
        'festival': Festival.objects.get(id =festival_id) ,
    }
    return render(request, "festivais/festival.html", context)


# Create your views here.
