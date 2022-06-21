# Generated by Django 4.0.4 on 2022-06-20 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comilon', '0003_compra_direccion_detalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='detalle',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Detalle',
        ),
        migrations.DeleteModel(
            name='Direccion',
        ),
    ]
