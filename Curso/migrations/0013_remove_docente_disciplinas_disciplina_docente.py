# Generated by Django 4.0.6 on 2024-05-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0012_remove_linguagens_de_programacoe_projetos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='disciplinas',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='docente',
            field=models.ManyToManyField(to='Curso.docente'),
        ),
    ]
