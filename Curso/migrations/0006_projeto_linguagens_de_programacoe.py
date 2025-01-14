# Generated by Django 4.0.6 on 2024-04-07 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0005_remove_projeto_disciplina_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_projeto', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('conceitos_aplicados', models.TextField()),
                ('tecnologias_utilizadas', models.TextField()),
                ('imagem', models.ImageField(upload_to='media/Curso')),
                ('link_youtube', models.URLField()),
                ('link_github', models.URLField()),
                ('disciplina', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Curso.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Linguagens_de_Programacoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_de_linguagem', models.CharField(max_length=100)),
                ('projetos', models.ManyToManyField(to='Curso.projeto')),
            ],
        ),
    ]
