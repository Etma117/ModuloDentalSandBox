# Generated by Django 4.2 on 2024-02-13 15:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinicas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinica',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='clinica',
            name='responsable',
        ),
        migrations.AddField(
            model_name='clinica',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='equipamiento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='hora_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='hora_inicio',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='numero_consultorios',
            field=models.IntegerField(help_text='Número de consultorios en la clínica (debe ser no negativo)', null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='clinica',
            name='responsables',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clinica',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
    ]
