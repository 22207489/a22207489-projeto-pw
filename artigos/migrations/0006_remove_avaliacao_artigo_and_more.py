# Generated by Django 4.0.6 on 2024-06-10 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='artigo',
        ),
        migrations.RemoveField(
            model_name='avaliacao',
            name='nome_avaliacao',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='artigo',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Artigo',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Avaliacao',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
