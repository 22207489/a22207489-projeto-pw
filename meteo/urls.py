from django.urls import path
from meteo import views
app_name = 'meteo'

urlpatterns = [
    path('tempo_lisboa/', views.lisboa_view, name='tempo_lisboa'),
    path('cinco_dias/',views.view_cinco_dias, name = 'cinco_dias'),
]