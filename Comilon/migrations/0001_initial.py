# Generated by Django 4.0.4 on 2022-06-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resgistro',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellido')),
                ('correo', models.CharField(max_length=100, verbose_name='correo electrónico')),
                ('clave', models.CharField(max_length=16, verbose_name='Clave')),
            ],
        ),
    ]
