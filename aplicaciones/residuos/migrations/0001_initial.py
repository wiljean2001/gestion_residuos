# Generated by Django 5.0.4 on 2024-04-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residuo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_recoleccion', models.DateField()),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidad_medida', models.CharField(max_length=50)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('peligrosidad', models.CharField(max_length=50)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('moneda', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
