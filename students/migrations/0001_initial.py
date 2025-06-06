# Generated by Django 4.2.20 on 2025-04-22 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del grupo')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Edad')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Correo electrónico')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Número de teléfono')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Dirección')),
                ('enrollment_date', models.DateField(auto_now_add=True, verbose_name='Fecha de inscripción')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='students.group', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Percentage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('partial', models.CharField(choices=[('1', '1er Parcial'), ('2', '2do Parcial'), ('3', '3er Parcial')], default='1', max_length=1, verbose_name='Parcial')),
                ('examen_points', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Puntos totales del examen')),
                ('assistances_amount', models.IntegerField(default=0, verbose_name='Cantidad de asistencias del parcial')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='percentages', to='students.group', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Porcentaje',
                'verbose_name_plural': 'Porcentajes',
                'unique_together': {('group', 'partial')},
            },
        ),
    ]
