# Generated by Django 4.0.6 on 2024-04-07 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandasNovas', '0004_alter_banda_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banda',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Banda',
        ),
        migrations.DeleteModel(
            name='Musica',
        ),
    ]
