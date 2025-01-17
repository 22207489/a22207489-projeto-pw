# Generated by Django 4.0.6 on 2024-04-07 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bandasNovas', '0002_delete_album_delete_banda_delete_musica'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano_de_lancamento', models.IntegerField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='media/bandas/')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.CharField(max_length=10)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nacionalidade_da_banda', models.CharField(max_length=100)),
                ('foto_da_banda', models.ImageField(blank=True, null=True, upload_to='media/bandas/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandasNovas.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='musica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandasNovas.musica'),
        ),
    ]
