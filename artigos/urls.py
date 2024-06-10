
from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'artigos'
urlpatterns = [

    #core do projeto
    path('', views.index_view, name='index'),
    path('autor/<int:autor_id>/', views.autor_view, name="autor"),
    path('artigo/<int:artigo_id>/', views.artigo_view, name="artigo"),
    path('comentario/<int:artigo_id>', views.comentario_view, name="comentario"),
    path('avaliacao/<int:artigo_id>', views.avaliacao_view, name="avaliacao"),


    #criar elementos
    path('autor/novo', views.novo_autor_view, name="novo_autor"),
    path('artigo/novo', views.novo_artigo_view,name="novo_artigo"),
    path('comentario/novo', views.novo_comentario_view, name="novo_comentario"),
    path('avaliacao/novo', views.novo_avaliacao_view, name="novo_avaliacao"),


    #Editar Elementos
    path('autor/edita/<int:autor_id>', views.edita_autor_view,name="edita_autor"),
    path('artigo/edita/<int:artigo_id>', views.edita_artigo_view,name="edita_artigo"),
    path('comentario/edita/<int:comentario_id>', views.edita_comentario_view,name="edita_comentario"),
    path('avaliacao/edita/<int:avaliacao_id>', views.edita_avaliacao_view,name="edita_avaliacao"),


    #Apagar elementos
    path('apaga_autor/<int:autor_id>', views.apaga_autor_view, name="apaga_autor"),
    path('apaga_artigo/<int:artigo_id>', views.apaga_artigo_view, name="apaga_artigo"),
    path('apaga_comentario/<int:comentario_id>', views.apaga_comentario_view, name="apaga_comentario"),
    path('apaga_avaliacao/<int:avaliacao_id>', views.apaga_avaliacao_view, name="apaga_avaliacao")


]