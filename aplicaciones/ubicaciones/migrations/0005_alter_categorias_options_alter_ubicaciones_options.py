# Generated by Django 5.0.6 on 2024-05-08 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0004_alter_categorias_options_alter_ubicaciones_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name_plural': 'ubicaciones-categorias'},
        ),
        migrations.AlterModelOptions(
            name='ubicaciones',
            options={'verbose_name_plural': 'ubicaciones-ubicaciones'},
        ),
    ]
