# Generated by Django 5.0.4 on 2024-04-23 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
        ('residuos', '0001_initial'),
        ('ubicaciones', '0001_initial'),
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recoleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia_numero', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('hora_recoleccion', models.TimeField()),
                ('peso_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=100)),
                ('residuo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residuos.residuo')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicaciones.ubicacion')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoRecojo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_en_recoleccion', models.CharField(choices=[('chofer', 'Chofer'), ('ayudante', 'Ayudante')], max_length=8)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personalrecojo')),
                ('recoleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recolecciones.recoleccion')),
            ],
        ),
    ]
