# Generated by Django 5.0.6 on 2024-05-08 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_alter_marcas_table_alter_modelos_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='marcas',
            table='vehiculos-marcas',
        ),
        migrations.AlterModelTable(
            name='modelos',
            table='vehiculos-modelos',
        ),
        migrations.AlterModelTable(
            name='vehiculos',
            table='vehiculos-vehiculos',
        ),
    ]