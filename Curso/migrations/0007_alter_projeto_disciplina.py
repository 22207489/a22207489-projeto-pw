# Generated by Django 4.0.6 on 2024-04-07 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0006_projeto_linguagens_de_programacoe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.disciplina'),
        ),
    ]
