from django.shortcuts import render



def continentes_view(request):
    return render(request, "novaapp/continentes.html")

def africa_view(request):
    return render(request, "novaapp/paisesAfrica.html")

def america_view(request):
    return render(request, "novaapp/paisesAmerica.html")

def antartica_view(request):
    return render(request, "novaapp/paisesAntartica.html")


def asia_view(request):
    return render(request, "novaapp/paisesAsia.html")


def europa_view(request):
    return render(request, "novaapp/paisesEuropa.html")


def oceania_view(request):
    return render(request, "novaapp/paisesOceania.html")
