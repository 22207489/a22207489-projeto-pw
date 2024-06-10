from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'portfolio'
urlpatterns = [

    #core do projeto
    path('', views.landing_view, name='landing'),
    path('about_me', views.me_by_me, name='about_me'),


]