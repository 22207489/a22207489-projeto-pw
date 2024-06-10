# Generated by Django 4.0.6 on 2024-04-20 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Curso', '0008_delete_curso_remove_disciplina_area_cientifica_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas_Cientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_area_cientifica', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_curso', models.CharField(max_length=100)),
                ('codigo_curso', models.IntegerField()),
                ('apresentacao', models.TextField()),
                ('objetivos', models.TextField()),
                ('condicoes_de_acesso', models.TextField()),
                ('oportunidades_de_carreira', models.TextField()),
                ('competencias', models.TextField()),
                ('creditos_do_curso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=100)),
                ('ects', models.IntegerField()),
                ('curricularIUnitReadableCode', models.CharField(max_length=100)),
                ('horas_totais', models.CharField(max_length=100)),
                ('area_cientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.areas_cientifica')),
            ],
        ),
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
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.disciplina')),
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
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_de_docente', models.CharField(max_length=100)),
                ('disciplinas', models.ManyToManyField(to='Curso.disciplina')),
            ],
        ),
    ]