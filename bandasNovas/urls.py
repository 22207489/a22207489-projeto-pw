from django.urls import path

from . import views

app_name = 'bandasNovas'

urlpatterns = [

    #Core das bandas
    path('', views.index_view, name="bandas"),
    path('banda/<int:banda_id>/', views.banda_view, name="banda"),
    path('album/<int:album_id>/', views.album_view, name="album"),
    path('musica/<int:musica_id>', views.musica_view, name="musica"),



    #Criar elementos
    path('cria_banda/', views.nova_banda_view, name="cria_banda"),
    path('cria_album/<int:banda_id>', views.novo_album_view, name="cria_album"),
    path('cria_musica/<int:album_id>', views.nova_musica_view, name="cria_musica"),



    #Edita elementos
    path('edita_banda/<int:banda_id>', views.edita_banda_view, name="edita_banda"),
    path('edita_album/<int:album_id>', views.edita_album_view, name="edita_album"),
    path('edita_musica/<int:musica_id>', views.edita_musica_view, name="edita_musica"),



    #Apaga elementos
     path('apaga_banda/<int:banda_id>', views.apaga_banda_view, name="apaga_banda"),
    path('apaga_album/<int:album_id>', views.apaga_album_view, name="apaga_album"),
    path('apaga_musica/<int:musica_id>', views.apaga_musica_view, name="apaga_musica")


]