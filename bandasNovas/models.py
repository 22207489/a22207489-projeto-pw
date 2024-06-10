from django.db import models
from django import forms    # formulários Django



class Banda(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade_da_banda = models.CharField(max_length=100)
    foto_da_banda = models.ImageField(upload_to='media/bandas/', null=True, blank=True)

    def __str__(self):
        return self.nome

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda
    fields = '__all__'











class Album(models.Model):
    titulo = models.CharField(max_length=100)
    ano_de_lancamento = models.IntegerField()
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    capa = models.ImageField(upload_to='media/bandas/', null=True, blank=True)
    def __str__(self):
        return self.titulo



class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = ['titulo','ano_de_lancamento','capa']







class Musica(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=10)
    link = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = ['nome','duracao','link']







