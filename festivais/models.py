from django.db import models


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    cartaz = models.ImageField(upload_to='media/festivais/', null=True, blank=True)
    festival = models.ManyToManyField(Banda, related_name = 'festivais')
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



















# Create your models here.
