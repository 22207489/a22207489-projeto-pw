from django.shortcuts import render


def landing_view(request):
    imagem =  'portfolio/Portfolio.JPG'
    video1 = 'portfolio/ Portfolio - Google Chrome 2024-06-10 22-53-11.mp4'
    video2 = 'portfolio/projeto1Pw _ _home_a22207489_projeto1Pw _ Directory Listing _ a22207489 _ PythonAnywhere - Google Chrome 2024-06-10 21-08-37.mp4'

    context = {
        'imagem' : imagem,
        'video1': video1,
        'video2':video2,
        }

    return render(request, "portfolio/landing.html",context)


def me_by_me(request):
    imagem =  'portfolio/Afonso Amaral - Resume (1).pdf'
    context = {
        'imagem' : imagem
        }

    return render(request, "portfolio/about_me.html",context)



# Create your views here.
