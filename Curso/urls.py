# bandas/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'curso'
urlpatterns = [

    #core do projeto
    path('', views.index_view, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_view, name="curso"),
    path('area/<int:area_id>/', views.area_cientifica_view, name="area"),
    path('disciplina/<int:disciplina_id>', views.disciplina_view, name="disciplina"),
    path('projeto/<str:projeto_id>', views.projeto_view, name="projeto"),


    #criar elementos
    path('curso/novo', views.novo_curso_view, name="novo_curso"),
    path('area/nova/<int:curso_id>', views.nova_area_view,name="nova_area"),
    path('disciplina/nova/<int:area_id>', views.nova_disciplina_view, name="nova_disciplina"),
    path('projeto/novo/<int:disciplina_id>', views.novo_projeto_view, name="novo_projeto"),
    path('linguagem/nova/<int:projeto_id>', views.nova_linguagem_view, name="nova_linguagem"),
    path('docente/novo/<int:disciplina_id>', views.novo_docente_view, name="novo_docente"),



    #Editar Elementos
    path('curso/edita/<int:curso_id>', views.edita_curso_view,name="edita_curso"),
    path('disciplina/edita/<int:disciplina_id>', views.edita_disciplina_view,name="edita_disciplina"),
    path('projeto/edita/<int:projeto_id>', views.edita_projeto_view,name="edita_projeto"),


    #Apagar elementos
    path('apaga_curso/<int:curso_id>', views.apaga_curso_view, name="apaga_curso"),
    path('apaga_area/<int:area_id>', views.apaga_area_view, name="apaga_area"),
    path('apaga_disciplina/<int:disciplina_id>', views.apaga_disciplina_view, name="apaga_disciplina"),
    path('apaga_projeto/<int:projeto_id>', views.apaga_projeto_view, name="apaga_projeto")


]