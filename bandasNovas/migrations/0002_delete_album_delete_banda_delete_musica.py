# Generated by Django 4.0.6 on 2024-04-07 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandasNovas', '0001_initial'),
    ]

    operations = [
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
