# Generated by Django 4.0.5 on 2023-06-27 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_vehiculomodel_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Permite ver el listado de vehiculos'),)},
        ),
    ]
