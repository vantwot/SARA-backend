# Generated by Django 4.2 on 2023-05-16 22:24

import Asignatura.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
                ('group', models.CharField(max_length=10)),
                ('prerequisite', models.JSONField(blank=True, default=Asignatura.models.prerequisiteDefault)),
                ('horario', models.JSONField(blank=True, default=Asignatura.models.horarioDefault)),
            ],
            options={
                'db_table': 'Asignatura',
            },
        ),
        migrations.CreateModel(
            name='EstudianteAsignatura',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_asignatura', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Asignatura.asignatura')),
            ],
            options={
                'db_table': 'EstudianteAsignatura',
            },
        ),
    ]
