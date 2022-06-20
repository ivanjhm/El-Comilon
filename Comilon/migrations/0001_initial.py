# Generated by Django 4.0.4 on 2022-06-13 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_Rol', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Rol')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre del Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_Usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Ususario')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo del Usuario')),
                ('clave', models.CharField(max_length=16, verbose_name='Clave del Usuario')),
                ('rut', models.CharField(max_length=11, verbose_name='Rut del usuario')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comilon.rol')),
            ],
        ),
    ]