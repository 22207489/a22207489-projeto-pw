from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('continentes/', views.continentes_view, name='continentes'),
    path('paisesAfrica/', views.africa_view, name='paisesAfrica'),
    path('paisesAmerica/', views.america_view, name='paisesAmerica'),
    path('paisesAntartica/', views.antartica_view, name='paisesAntartica'),
    path('paisesAsia/', views.asia_view, name='paisesAsia'),
    path('paisesEuropa/', views.europa_view, name='paisesEuropa'),
    path('paisesOceania/', views.oceania_view, name='paisesOceania'),


]