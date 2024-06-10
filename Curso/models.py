from django.db import models
from django import forms    # formulários Django


#Curso
class Curso(models.Model):
    nome_do_curso = models.CharField(max_length=100)
    codigo_curso = models.IntegerField()
    apresentacao = models.TextField()
    objetivos = models.TextField()
    condicoes_de_acesso = models.TextField()
    oportunidades_de_carreira = models.TextField()
    competencias = models.TextField()
    creditos_do_curso = models.IntegerField()

    def __str__(self):
        return self.nome_do_curso


class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'








#Area cientifica
class Areas_Cientifica(models.Model):
    nome_area_cientifica = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_area_cientifica

class Areas_CientificaForm(forms.ModelForm):
  class Meta:
    model = Areas_Cientifica
    fields = ['nome_area_cientifica']

    labels = {
        'nome_area_cientifica': 'Nome da Área Cientifica',
    }





#Docente
class Docente(models.Model):
    nome_de_docente = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_de_docente

class DocenteForm(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'












#Disciplina
class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=100)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=100)
    area_cientifica = models.ForeignKey(Areas_Cientifica, on_delete=models.CASCADE)
    horas_totais = models.CharField(max_length=100)
    docente = models.ManyToManyField(Docente)

    def __str__(self):
        return self.nome_disciplina

class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = ['nome_disciplina','ano','semestre','ects','curricularIUnitReadableCode','horas_totais','docente']













#Libguagnes de programacao
class Linguagens_de_Programacoe(models.Model):
    nome_de_linguagem = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_de_linguagem

class Linguagens_de_ProgramacoeForm(forms.ModelForm):
  class Meta:
    model = Linguagens_de_Programacoe
    fields = '__all__'









#Projetos
class Projeto(models.Model):
    nome_do_projeto = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_utilizadas = models.ManyToManyField(Linguagens_de_Programacoe)
    imagem = models.ImageField(upload_to='media/Curso')
    link_youtube = models.URLField()
    link_github = models.URLField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_do_projeto

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = ['nome_do_projeto','descricao','conceitos_aplicados','tecnologias_utilizadas','imagem','link_youtube','link_github']
























